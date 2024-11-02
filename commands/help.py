async def help_command(message):
    help_text = (
        "**Available Commands:**\n"
        "`&ping` - Check the bot's latency.\n"
        "`&wiki \"Character Name\"` - Fetch details about a specific OS-tan character.\n"
        "`&info` - Get information about the bot.\n"
    )
    await message.channel.send(help_text)
