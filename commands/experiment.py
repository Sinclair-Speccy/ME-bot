from discord import Embed

async def execute(client, message):
    embed = Embed(
        title="Bot Experiment Notice",
        color=0x00FF00      )
    
    embed.add_field(
        name="Purpose of This Bot",
        value=(
            "This bot is an experimental project to test a theory: whether a bot can present character information "
            "and data in a way that reduces the need to visit external wikis. The goal is to make it easier for users "
            "to access relevant details directly in the server."
        ),
        inline=False
    )
    embed.add_field(
        name="Live Testing Notice",
        value=(
            "⚠️ **Please note**: This bot is in constant development and is tested live. As a result, some commands may "
            "not work as expected or may be changed frequently. Please be patient as I refine and improve the bot."
        ),
        inline=False
    )
    embed.add_field(
        name="Frequent Restarts & Downtime",
        value=(
            "The bot may go offline periodically as I implement updates, fix bugs, or test new features. This means you "
            "might see it go on and off as changes are manually applied."
        ),
        inline=False
    )
    
    embed.set_footer(text="Thank you for helping test this experimental bot!")
    
    await message.channel.send(embed=embed)
