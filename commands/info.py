from discord import Embed

# Replace hardcoded values with configurable options
BOT_VERSION = "1.5"
CREATOR = "sinclairspeccy75"
GITHUB_REPO = "https://github.com/Sinclair-Speccy/ME-bot"

async def execute(client, message):
    try:
        embed = Embed(
            title="Bot Information",
            color=0x00FF00
        )

        embed.add_field(name="Version", value=BOT_VERSION, inline=True)
        embed.add_field(name="Created by", value=CREATOR, inline=True)
        embed.add_field(
            name="Purpose",
            value="To provide information about OS-tan characters and related content.",
            inline=False
        )
        embed.add_field(
            name="How to Use",
            value="Type a command starting with `&` to interact with the bot.",
            inline=False
        )
        embed.add_field(
            name="Contributions and Removals",
            value=(
                "Contributions are welcome! Visit the GitHub [repository](https://github.com/Sinclair-Speccy/ME-bot) "
                "for details on adding or removing content."
            ),
            inline=False
        )
        embed.add_field(
            name="License",
            value=(
                "This project is licensed under **GPL-3.0**. You can use, share, and modify it, "
                "but must retain the same license and make the source code available."
            ),
            inline=False
        )

        embed.set_footer(text="Thank you for using ME-Tan!")

        await message.channel.send(embed=embed)

    except Exception as e:
        print(f"An error occurred while sending the bot information embed: {e}")
        await message.channel.send("An error occurred while retrieving bot information. Please try again later.")
