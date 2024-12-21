import discord  # Import discord explicitly

async def mehelp_command(bot, ctx):
    help_text = (
        "**Available Commands:**\n"
        "`&ping` - Check the bot's latency.\n"
        "`&wiki \"Character Name\"` - Fetch details about a specific OS-tan character.\n"
        "`&info` - Get information about the bot.\n"
        "`&copyright \"Character Name\"` - Get copyright details for a specific character.\n"
        "`&experiment` - Learn about the bot's experimental purpose and testing status.\n"
        "`&status` - View the bot's status, including uptime, latency, and server stats.\n"
        "`&image` - Placeholder for future image-fetching functionality.\n"
    )

    embed = discord.Embed(
        title="ME-Tan Help Commands",
        description=help_text,
        color=0x00FF00
    )
    embed.set_footer(text="For additional assistance, contact the bot's creator.")
    await ctx.channel.send(embed=embed)
