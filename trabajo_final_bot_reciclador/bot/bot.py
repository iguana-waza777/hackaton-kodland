import discord
from discord.ext import commands
from bot import setup_commands
import os
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"✅ Bot conectado como {bot.user}")

    setup_commands(bot)

    bot.run(TOKEN)
