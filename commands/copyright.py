import json
import os
import re
from discord import Embed
import logging

logging.basicConfig(level=logging.INFO)

async def execute(client, message):
    command_prefix = '&copyright'
    command_pattern = rf'{re.escape(command_prefix)} "(.+?)"'

    if not re.search(command_pattern, message.content):
        embed = Embed(
            title="Copyright Information",
            description=(
                "Not all characters have documented copyright statuses. "
                "By default, characters are assumed to be released under fair use unless otherwise stated. "
                "If a character has a specific copyright, they will have a dedicated copyright entry.\n\n"
                "Characters' copyright statuses may vary depending on the source. For example, character wikis or licenses may utilize different license types such as CC BY, CC BY-NC, or CC0 (Public Domain).\n\n"
                "To view the copyright information for a specific character, please use the command:\n\n"
                "`&copyright \"Character Name\"`\n\n"
                "For example:\n"
                "`&copyright \"Me-tan\"`"
            ),
            color=0x00FF00
        )
        await message.channel.send(embed=embed)
        return

    query = re.search(command_pattern, message.content).group(1).strip()
    logging.info(f"Received copyright query: {query}")

    try:
        with open('D:\\Code\\ME-bot\\copyrights\\copyright_files.json', 'r', encoding='utf-8') as file_list:
            copyright_files = json.load(file_list)
    except FileNotFoundError:
        logging.error("Main copyright file not found.")
        await message.channel.send("An error occurred while trying to access copyright data.")
        return

    if query not in copyright_files:
        await message.channel.send(
            "I couldn't find a copyright entry for that query. "
            "Please check if the name is correct or if it has been added yet."
        )
        return

    copyright_file_path = f'D:\\Code\\ME-bot\\copyrights\\{copyright_files[query]}'
    if not os.path.exists(copyright_file_path):
        await message.channel.send(f"No data available for '{query}'.")
        return

    try:
        with open(copyright_file_path, 'r', encoding='utf-8') as copyright_file:
            copyright_data = json.load(copyright_file)
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON data from file: {copyright_file_path}")
        await message.channel.send("There was an error reading the copyright data for this character.")
        return

    embed = Embed(
        title=copyright_data.get("title", "Copyright Information"),
        color=0x0099FF
    )
    embed.add_field(name="Holder", value=copyright_data.get("holder", "Unknown"), inline=False)
    embed.add_field(name="License", value=copyright_data.get("license", "Unknown"), inline=False)
    embed.add_field(name="Terms", value=copyright_data.get("terms", "No terms available."), inline=False)

    source = copyright_data.get("source")
    if source:
        embed.add_field(name="Source", value=f"[Link]({source})", inline=False)
    else:
        embed.add_field(name="Source", value="No source available.", inline=False)

    embed.set_footer(text="Fetched from internal copyright data")

    await message.channel.send(embed=embed)
