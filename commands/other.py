from discord import Embed

async def explain_exclusions(client, message):
    try:
        embed = Embed(
            title="Character Exclusion Policy",
            description="This document outlines why certain characters are excluded from the bot.",
            color=0x00FF00
        )

        embed.add_field(
            name="Not Computer-Related",
            value=(
                "This is a case-by-case decision, but characters not related to computers, software, or technology (like OS-tans) "
                "are generally not included as they don't align with the bot's theme."
            ),
            inline=False
        )
        embed.add_field(
            name="Licenses",
            value=(
                "Some fan universes have their own licenses created by their authors, which may limit the ability to add those characters. "
                "To simplify content management, the bot only includes characters assumed to be under free-use conditions, without taking credit."
            ),
            inline=False
        )
        embed.add_field(
            name="Permission",
            value=(
                "Characters will **not** be added unless explicit permission is granted by their **original creator**. "
                "Requests to add such characters will be denied automatically unless you are the creator."
            ),
            inline=False
        )

        embed.set_footer(text=f"Thanks for understanding! | Requested in {message.guild.name}" if message.guild else "Thanks for understanding!")

        await message.channel.send(embed=embed)

    except Exception as e:
        print(f"An error occurred in explain_exclusions: {e}")
        await message.channel.send("An error occurred while trying to display the exclusion policy. Please try again later.")
