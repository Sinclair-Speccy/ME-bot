from discord import Embed

async def execute(client, message):
    embed = Embed(
        title="Bot Information",
        color=0x00FF00
    )
    
    embed.add_field(name="Version", value="1.0", inline=False)
    embed.add_field(name="Created by", value="sinclairspeccy75", inline=False)
    embed.add_field(name="Purpose", value="To provide information about OS-tan characters and related content.", inline=False)
    embed.add_field(name="Commands Available", value="`&wiki`, `&ping`, `&info`, etc.", inline=False)
    embed.add_field(name="How to Use", value="Type a command starting with '&' to interact with the bot.", inline=False)
    embed.add_field(name="Contributions and Removals", value="Contributions are welcome! See the GitHub [repo](https://github.com/Sinclair-Speccy/ME-bot) for more details on adding or removing content.", inline=False)
    embed.add_field(name="License", value="This project is licensed under GPL-3.0. You can use, share, and modify it, but must keep the same license and make source code available.", inline=False)
    
    embed.set_footer(text="Thank you for using ME-Tan!")
    
    await message.channel.send(embed=embed)
