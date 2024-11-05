from discord import Embed

async def explain_exclusions(client, message):
    embed = Embed(
        title="Character Exclusion Policy",
        color=0x00FF00
    )
    
    embed.add_field(
        name="Not Computer-Related",
        value="This is a hit or miss thing, but not all characters are like OS-tans or in a similar vein, so there's no point adding them.",
        inline=False
    )
    embed.add_field(
        name="Licenses",
        value="This more applies to fan universes but each one there has its own license made by its creator, which could limit whether characters get added. I prefer not to deal with separate licenses. When I add content to the bot, everything is under the assumption of free use, as long as I'm not taking credit.",
        inline=False
    )
    embed.add_field(
        name="Permission",
        value="Unless I am given permission by the *creator* themselves, characters will **not** be added. Requests to add them will be denied automatically unless you are the creator.",
        inline=False
    )
    
    embed.set_footer(text="Thanks for understanding!")
    
    await message.channel.send(embed=embed)
