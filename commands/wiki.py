import json
import os
import re
import logging
from discord import Embed

logging.basicConfig(level=logging.INFO)

# Base directory configuration
CHARACTERS_DIR = os.getenv("CHARACTERS_DIR", "D:\\Code\\ME-bot\\characters\\")

async def execute(bot, ctx):
    command_prefix = '&wiki'
    command_pattern = re.compile(rf'{re.escape(command_prefix)}\s*"([^"]+)"')

    match = re.search(command_pattern, ctx.message.content)

    # Show usage instructions if no valid match is found
    if not match:
        await ctx.send(
            embed=Embed(
                title="How to Use the Wiki Command",
                description=(
                    'To search for a character, use quotation marks around the character\'s name, e.g., `&wiki "Windows 95-tan"`.\n\n'
                    'If the bot doesn\'t find the character, it might not be added yet or there could be issues with the data. '
                    'Content is retrieved from OS-tan Collections and licensed under Attribution-Non-Commercial-Share Alike 2.0 France.'
                ),
                color=0x00FF00
            )
        )
        return

    query = match.group(1).strip()
    logging.info(f"Received query: {query}")

    # Load character aliases
    aliases_file = os.path.join(CHARACTERS_DIR, "character_aliases.json")
    try:
        with open(aliases_file, 'r', encoding='utf-8') as alias_file:
            aliases = json.load(alias_file)
    except FileNotFoundError:
        logging.error(f"Aliases file not found: {aliases_file}")
        await ctx.send("An error occurred while accessing character data.")
        return

    # Find matching characters
    matching_characters = {
        name: data["character_file"]
        for name, data in aliases.items()
        if query.lower() in map(str.lower, data["aliases"])
    }
    logging.info(f"Matching characters: {matching_characters}")

    if not matching_characters:
        await ctx.send(
            embed=Embed(
                title="Character Not Found",
                description=(
                    "I couldn't find a character matching your query. Check the name and try again. "
                    "If it exists, it may not yet be added to the bot's data."
                ),
                color=0xFF0000
            )
        )
        return

    if len(matching_characters) > 1:
        options = "\n".join([f"{i + 1}. {name}" for i, name in enumerate(matching_characters.keys())])
        await ctx.send(
            embed=Embed(
                title="Multiple Matches Found",
                description=f"Found multiple matches for '{query}':\n\n{options}\n\n"
                            "To get your chosen character, rerun the command with '-tan' at the end unless it's a character like Nyake.",
                color=0x00FF00
            )
        )
        return

    # Handle single character match
    await handle_character_response(bot, ctx, list(matching_characters.values())[0])


async def handle_character_response(bot, ctx, character_file):
    logging.info(f"Selected character file: {character_file}")
    character_file_path = os.path.join(CHARACTERS_DIR, character_file)

    if not os.path.exists(character_file_path):
        logging.warning(f"Character file not found: {character_file_path}")
        await ctx.send(
            embed=Embed(
                title="Character Data Missing",
                description=f"No character data available for '{character_file}'.",
                color=0xFF0000
            )
        )
        return

    try:
        with open(character_file_path, 'r', encoding='utf-8') as file:
            character_data = json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error in file {character_file_path}: {e}")
        await ctx.send("There was an error reading the character data.")
        return

    # Create an embed for character details
    embed = Embed(
        title=character_data.get("name", "Character Information"),
        url=character_data.get("page_link"),
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

    embed.set_footer(text="Data retrieved as-is from the OSC wiki. Note that the wiki may contain outdated information.")

    await ctx.send(embed=embed)
