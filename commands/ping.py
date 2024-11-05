import discord
from discord import Embed

async def execute(client, message):
    latency = round(client.latency * 1000)
    embed = Embed(
        title="Pong! 🏓",
        description=f"Latency is {latency}ms",
        color=0x00FF00
    )
    await message.channel.send(embed=embed)
