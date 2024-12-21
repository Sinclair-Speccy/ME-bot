from discord import Embed

async def execute(client, message):
    try:
        embed = Embed(
            title="Bot Experiment Notice",
            color=0x00FF00  # Green for general information
        )

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
            name="⚠️ Live Testing Notice",
            value=(
                "This bot is in constant development and is tested live. As a result, some commands may not work as "
                "expected or may change frequently. Please be patient as I refine and improve the bot."
            ),
            inline=False
        )
        embed.add_field(
            name="Frequent Restarts & Downtime",
            value=(
                "The bot may go offline periodically as updates, bug fixes, or new features are tested. You may see it "
                "go on and off as changes are manually applied."
            ),
            inline=False
        )

        # Add a dynamic footer with server name if available
        if message.guild:
            footer_text = f"Thank you for helping test this experimental bot on {message.guild.name}!"
        else:
            footer_text = "Thank you for helping test this experimental bot!"
        embed.set_footer(text=footer_text)

        await message.channel.send(embed=embed)

    except Exception as e:
        # Log and notify the user if the message fails to send
        print(f"Error sending embed: {e}")
        await message.channel.send("An error occurred while trying to send the embed message.")
