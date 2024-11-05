import discord
import json
from utils import read_config
from commands import ping, wiki, info, help_command, execute_copyright, experiment

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
        return

    print(f'Received message: {message.content}')

    if message.content.startswith(config['prefix'] + 'ping'):
        print('Ping command detected')
        await ping(client, message)
    elif message.content.startswith(config['prefix'] + 'wiki'):
        print('Wiki command detected')
        await wiki(client, message)
    elif message.content.startswith(config['prefix'] + 'help'):
        print('Help command detected')
        await help_command(client, message)
    elif message.content.startswith(config['prefix'] + 'info'):
        print('Info command detected')
        await info(client, message)
    elif message.content.startswith(config['prefix'] + 'copyright'):
        print('Copyright command detected')
        await execute_copyright(client, message)
    elif message.content.startswith(config['prefix'] + 'experiment'):  # Add this block
        print('Experiment command detected')
        await experiment(client, message)

client.run(config['login']['token'])
