import json
import os
import re
import logging
from discord import Embed

# Configure logging
logging.basicConfig(level=logging.INFO)

async def execute(client, message):
    command_prefix = '&wiki'
    command_pattern = rf'{re.escape(command_prefix)} "(.+?)"'

    if not re.search(command_pattern, message.content):
        await message.channel.send('Please use quotation marks around the character\'s name, e.g., `&wiki "Windows 95-tan"`')
        return

    query = re.search(command_pattern, message.content).group(1).strip()
    logging.info("Received query: %s", query)

    # Load aliases from the alias file with UTF-8 encoding
    with open('D:\\Code\\ME-bot\\characters\\character_aliases.json', 'r', encoding='utf-8') as alias_file:
        aliases = json.load(alias_file)
    logging.info("Loaded aliases: %s", aliases)

    # Find all characters corresponding to the query
    matching_characters = {name: data["character_file"] for name, data in aliases.items() if query in data["aliases"]}
    
    if not matching_characters:
        await message.channel.send(
            "I couldn't find a character matching your query. Please check if the name is correct. "
            "If you're sure it exists, there might be an issue with the character data in the JSON file, "
            "or it hasn't been added yet. It's also possible that the character is listed on the wiki but has no entry. "
            "In any case, if the wiki doesn't have a page for it, please don’t blame me!".replace(" ", "\u00A0")
        )
        return
    
    if len(matching_characters) > 1:
        options = '\n'.join([f"{i+1}. {name}" for i, name in enumerate(matching_characters.keys())])
        await message.channel.send(f"There are multiple characters for '{query}':\n{options}\nPlease specify which one you mean by typing the number, or rerun the command with the character's full name, e.g., `&wiki \"OSC Windows 1.0\"`.")
        return

    # Proceed with the single match
    await handle_character_response(client, message, list(matching_characters.values())[0])

async def handle_character_response(client, message, character_file):
    logging.info("Selected character file: %s", character_file)
    character_file_path = f'D:\\Code\\ME-bot\\characters\\{character_file}'
    
    if not os.path.exists(character_file_path):
        await message.channel.send(f"No character data available for '{character_file}'.")
        return

    # Load character data from JSON file
    with open(character_file_path, 'r') as file:
        character_data = json.load(file)

    # Prepare the embed
    embed = Embed(
        title=character_data["name"],
        url=character_data["page_link"],
        color=0x0099FF
    )

    # Add character information to the embed
    embed.add_field(name="First Appearance", value=character_data.get("first_appearance", "Unknown"), inline=False)
    embed.add_field(name="Hair Color", value=character_data.get("hair_color", "Unknown"), inline=False)
    embed.add_field(name="Eye Color", value=character_data.get("eye_color", "Unknown"), inline=False)
    embed.add_field(name="Common Names", value=character_data.get("common_names", "Unknown"), inline=False)
    embed.add_field(name="Faction", value=character_data.get("faction", "Unknown"), inline=False)
    embed.add_field(name="Lineage", value=character_data.get("lineage", "Unknown"), inline=False)
    embed.add_field(name="Rivals", value=character_data.get("rivals", "Unknown"), inline=False)
    embed.add_field(name="Height", value=character_data.get("height", "Unknown"), inline=False)

    # Add character details
    character_details = character_data.get("character_details", "No character details available.")
    embed.add_field(name="Character Details", value=character_details, inline=False)

    embed.set_footer(text='Fetched from OS-tan Collections')
    await message.channel.send(embed=embed)

async def on_message(client, message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check for commands
    if message.content.startswith('&wiki'):
        await execute(client, message)
