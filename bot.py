import discord
from discord.ext import commands
import time
import logging
from commands import ping, wiki, info, help_command, execute_copyright, experiment, status, image
from utils import read_config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load configuration
try:
    config = read_config("config.json")  # Specify the file path for clarity
    bot_token = config.get("login", {}).get("token")
    command_prefix = config.get("prefix", "&")
    if not bot_token:
        raise ValueError("Bot token is missing in config.json")
except FileNotFoundError:
    logger.error("Config file 'config.json' not found. Ensure the file exists.")
    raise
except ValueError as e:
    logger.error(f"Configuration error: {e}")
    raise
except Exception as e:
    logger.error(f"Failed to load configuration: {e}")
    raise

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

# Record bot start time
bot.start_time = time.time()

# Events
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user}')

# Commands
@bot.command(name='ping')
async def ping_command(ctx):
    logger.info(f'Ping command invoked by {ctx.author} in {ctx.guild.name if ctx.guild else "DM"}')
    await ping(bot, ctx)

@bot.command(name='wiki')
async def wiki_command(ctx):
    logger.info(f'Wiki command invoked by {ctx.author}')
    await wiki(bot, ctx)

# Remove the default help command
bot.remove_command("help")

@bot.command(name='help')
async def help_command_fn(ctx):
    logger.info(f'Help command invoked by {ctx.author}')
    await help_command(bot, ctx)

@bot.command(name='info')
async def info_command(ctx):
    logger.info(f'Info command invoked by {ctx.author}')
    await info(bot, ctx)

@bot.command(name='copyright')
async def copyright_command(ctx):
    logger.info(f'Copyright command invoked by {ctx.author}')
    await execute_copyright(bot, ctx)

@bot.command(name='experiment')
async def experiment_command(ctx):
    logger.info(f'Experiment command invoked by {ctx.author}')
    await experiment(bot, ctx)

@bot.command(name='status')
async def status_command(ctx):
    logger.info(f'Status command invoked by {ctx.author}')
    await status(bot, ctx)

@bot.command(name='image')
async def image_command(ctx):
    logger.info(f'Image command invoked by {ctx.author}')
    await image(bot, ctx)

# Run the bot
try:
    bot.run(bot_token)
except discord.LoginFailure:
    logger.error("Invalid bot token. Please check your config.json.")
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
