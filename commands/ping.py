import discord
from discord import Embed

async def execute(client, message):
    try:
        latency = round(client.latency * 1000)
        
        # Provide feedback based on latency value
        if latency < 100:
            status = "Excellent 👍"
        elif latency < 200:
            status = "Good 😊"
        elif latency < 300:
            status = "Moderate 🤔"
        else:
            status = "Poor 😟"

        embed = Embed(
            title="Pong! 🏓",
            description=(
                f"**Latency:** {latency}ms\n"
                f"**Status:** {status}"
            ),
            color=0x00FF00
        )

        embed.set_footer(text="Bot Latency Check")
        await message.channel.send(embed=embed)

    except discord.Forbidden:
        print("Bot lacks permissions to send messages in this channel.")
    except Exception as e:
        print(f"An error occurred in the ping command: {e}")
        await message.channel.send("An unexpected error occurred. Please try again later.")
