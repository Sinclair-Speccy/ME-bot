import json
import os
import re
import logging
from discord import Embed

logging.basicConfig(level=logging.INFO)

async def execute(client, message):
    command_prefix = '&wiki'
    command_pattern = rf'{re.escape(command_prefix)} "(.+?)"'

    if not re.search(command_pattern, message.content):
        embed = Embed(
            title="How to Use the Wiki Command",
            description=(
                'To search for a character, use quotation marks around the character\'s name, e.g., `&wiki "Windows 95-tan"`.\n\n'
                'Sometimes you may need to add the -tan part as this bot is a WIP.\n\n'
                'Information is retrieved from OS-tan Collections and content is available under Attribution-Non-Commercial-Share Alike 2.0 France unless otherwise noted. '
                'This license allows use with credit provided, included in each character entry on the footer text.'
            ),
            color=0x00FF00
        )
        await message.channel.send(embed=embed)
        return

    query = re.search(command_pattern, message.content).group(1).strip()
    logging.info(f"Received query: {query}")

    with open('D:\\Code\\ME-bot\\characters\\character_aliases.json', 'r', encoding='utf-8') as alias_file:
        aliases = json.load(alias_file)
    logging.info(f"Loaded aliases: {aliases}")

    matching_characters = {name: data["character_file"] for name, data in aliases.items() if query in data["aliases"]}
    
    if not matching_characters:
        error_embed = Embed(
            title="Character Not Found",
            description=(
                "I couldn't find a character matching your query. Please check if the name is correct. "
                "If it exists, there might be an issue with the character data in the JSON file, "
                "or it hasn't been added yet. If the wiki doesn't have a page, please don’t blame me!"
            ),
            color=0xFF0000  # Red color for error
        )
        await message.channel.send(embed=error_embed)
        return

    if len(matching_characters) > 1:
        options = '\n'.join([f"{i+1}. {name}" for i, name in enumerate(matching_characters.keys())])
        await message.channel.send(
            f"There are multiple characters for '{query}':\n{options}\n"
            "Specify which one you mean by typing the number or rerun the command with the full name, e.g., `&wiki \"OSC Windows 1.0\"`."
        )
        return

    await handle_character_response(client, message, list(matching_characters.values())[0])

async def handle_character_response(client, message, character_file):
    logging.info(f"Selected character file: {character_file}")
    character_file_path = f'D:\\Code\\ME-bot\\characters\\{character_file}'
    
    if not os.path.exists(character_file_path):
        await message.channel.send(f"No character data available for '{character_file}'.")
        return

    with open(character_file_path, 'r', encoding='utf-8') as file:
        character_data = json.load(file)

    embed = Embed(
        title=character_data["name"],
        url=character_data["page_link"],
        color=0x00FF00
    )

    embed.add_field(name="First Appearance", value=character_data.get("first_appearance", "Unknown"), inline=False)
    embed.add_field(name="Hair Color", value=character_data.get("hair_color", "Unknown"), inline=False)
    embed.add_field(name="Eye Color", value=character_data.get("eye_color", "Unknown"), inline=False)
    embed.add_field(name="Common Names", value=character_data.get("common_names", "Unknown"), inline=False)
    embed.add_field(name="Faction", value=character_data.get("faction", "Unknown"), inline=False)
    embed.add_field(name="Lineage", value=character_data.get("lineage", "Unknown"), inline=False)
    embed.add_field(name="Rivals", value=character_data.get("rivals", "Unknown"), inline=False)
    embed.add_field(name="Height", value=character_data.get("height", "Unknown"), inline=False)
    embed.add_field(name="Character Details", value=character_data.get("character_details", "No character details available."), inline=False)

    embed.set_footer(text='Data retrieved as-is from the OSC wiki. Note that the wiki may contain outdated information.')

    await message.channel.send(embed=embed)
