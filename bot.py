import discord
import json
from utils import read_config
from commands import ping, wiki, info  # Importing the new commands

# Load the config file
config = read_config()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    print(f'Received message: {message.content}')  # Log received messages
    
    if message.content.startswith(config['prefix'] + 'ping'):
        print('Ping command detected')  # Log ping command detection
        await ping.execute(client, message)
    elif message.content.startswith(config['prefix'] + 'wiki'):
        print('Wiki command detected')  # Log wiki command detection
        await wiki.execute(client, message)
    elif message.content.startswith(config['prefix'] + 'help'):
        print('Help command detected')  # Log help command detection
        await help_command.execute(client, message)  # Call help command
    elif message.content.startswith(config['prefix'] + 'info'):
        print('Info command detected')  # Log info command detection
        await info.execute(client, message)  # Corrected to use 'info'
    elif message.content.startswith(config['prefix'] + 'count'):
        print('Character count command detected')  # Log character count command detection
        await character_count_command.execute(client, message)  # Call character count command
    elif message.content.startswith(config['prefix'] + 'clear'):
        print('Clear command detected')  # Log clear command detection
        try:
            num_messages = int(message.content.split()[1])  # Get the number of messages to delete
            await clear_command.execute(client, message, num_messages)  # Call clear command
        except (IndexError, ValueError):
            await message.channel.send("Please provide a valid number of messages to delete.")

client.run(config['login']['token'])
