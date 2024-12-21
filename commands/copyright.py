import json
import os
import re
from discord import Embed
import logging

logging.basicConfig(level=logging.INFO)

# Function to execute copyright command
async def execute(client, ctx):
    command_prefix = '&copyright'
    command_pattern = re.compile(rf'{re.escape(command_prefix)}\s*"([^"]+)"')

    match = re.search(command_pattern, ctx.message.content)

    # If no match is found, send usage instructions
    if not match:
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
        await ctx.send(embed=embed)
        return

    query = match.group(1).strip()
    logging.info(f"Received copyright query: {query}")

    # Load copyright file index
    config_path = os.getenv('COPYRIGHT_INDEX_PATH', 'D:\\Code\\ME-bot\\copyrights\\copyright_files.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as file_list:
            copyright_files = json.load(file_list)
    except FileNotFoundError:
        logging.error(f"Copyright index file not found at {config_path}")
        await ctx.send("An error occurred while trying to access copyright data. Please try again later.")
        return

    # Check if the query exists in the index
    if query not in copyright_files:
        await ctx.send(
            f"I couldn't find a copyright entry for '{query}'. "
            "Please check if the name is correct or if it has been added yet."
        )
        return

    # Construct file path for the specific character
    copyright_file_path = os.path.join(
        os.path.dirname(config_path), copyright_files[query]
    )

    # Ensure the file exists
    if not os.path.exists(copyright_file_path):
        logging.warning(f"File for '{query}' not found: {copyright_file_path}")
        await ctx.send(f"No data available for '{query}'. Please try again later.")
        return

    # Load specific copyright data
    try:
        with open(copyright_file_path, 'r', encoding='utf-8') as copyright_file:
            copyright_data = json.load(copyright_file)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON file {copyright_file_path}: {e}")
        await ctx.send("There was an error reading the copyright data for this character.")
        return

    # Build embed response
    embed = Embed(
        title=copyright_data.get("title", "Copyright Information"),
        color=0x0099FF
    )
    embed.add_field(name="Holder", value=copyright_data.get("holder", "Unknown"), inline=False)
    embed.add_field(name="License", value=copyright_data.get("license", "Unknown"), inline=False)
    embed.add_field(name="Terms", value=copyright_data.get("terms", "No terms available."), inline=False)

    # Add source if available
    source = copyright_data.get("source")
    if source:
        embed.add_field(name="Source", value=f"[Link]({source})", inline=False)
    else:
        embed.add_field(name="Source", value="No source available.", inline=False)

    # Add footer
    embed.set_footer(text="Fetched from internal copyright data")

    # Send the embed
    await ctx.send(embed=embed)
