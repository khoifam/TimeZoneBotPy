import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def setup_hook():
    await bot.load_extension("ping_pong_cog")
    await bot.load_extension("time_zone_cog")

@bot.event
async def on_ready():
    print("Logged in")

@bot.event
async def on_command_error(ctx, error):
    pass

@bot.event
async def on_message(msg):
    if msg.content == "asdf":
        print("asdf")
    await bot.process_commands(msg)

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)