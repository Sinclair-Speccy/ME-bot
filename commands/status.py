import discord
from datetime import datetime

bot_start_time = datetime.utcnow()

async def execute(client, message):
    current_time = datetime.utcnow()
    uptime = current_time - bot_start_time  # Calculate uptime

    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)  # Convert seconds into hours
    minutes, _ = divmod(remainder, 60)  # Convert remaining seconds into minutes

    guild = message.guild  # Get the server (guild) from the message
    total_users = guild.member_count  # Total number of members
    online_users = sum(1 for member in guild.members if member.status != discord.Status.offline)  # Count of online users
    active_channels = len(guild.text_channels) + len(guild.voice_channels)  # Active channels (text + voice)
    bot_latency = round(client.latency * 1000)  # Get the latency in milliseconds

    embed = discord.Embed(
        title="Bot Status",
        description=(
            f"**Status:** Online\n"
            f"**Uptime:** {days}d {hours}h {minutes}m\n"
            f"**Total Users:** {total_users}\n"
            f"**Online Users:** {online_users}\n"
            f"**Active Channels:** {active_channels}\n"
            f"**Bot Latency:** {bot_latency}ms\n"
        ),
        color=0x00FF00
    )
    await message.channel.send(embed=embed)
