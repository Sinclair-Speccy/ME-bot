from discord import Embed

async def execute(client, message):
    help_text = (
        "**Available Commands:**\n"
        "`&ping` - Check the bot's latency.\n"
        "`&wiki \"Character Name\"` - Fetch details about a specific OS-tan character.\n"
        "`&info` - Get information about the bot.\n"
        "`&copyright \"Character Name\"` - Get copyright details for a specific character.\n"
    )
    embed = Embed(
        title="ME-Tan Help Commands",
        description=help_text,
        color=0x00FF00
    )
    await message.channel.send(embed=embed)
