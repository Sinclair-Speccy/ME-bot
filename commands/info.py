from discord import Embed

async def execute(client, message):
    # Create an embed for better formatting
    embed = Embed(
        title="Bot Information",
        color=0x0099FF  # You can choose any color you like
    )
    
    # Add fields with information about the bot
    embed.add_field(name="Version", value="1.0", inline=False)
    embed.add_field(name="Created by", value="sinclairspeccy75", inline=False)
    embed.add_field(name="Purpose", value="To provide information about OS-tan characters and related content.", inline=False)
    embed.add_field(name="Commands Available", value="`&wiki`, `&ping`, `&info`, etc.", inline=False)
    embed.add_field(name="How to Use", value="Type a command starting with '&' to interact with the bot.", inline=False)
    embed.add_field(name="Support", value="For any issues, contact the developer.", inline=False)
    
    # Optionally add a footer
    embed.set_footer(text="Thank you for using ME-Tan!")

    # Send the embed message
    await message.channel.send(embed=embed)
