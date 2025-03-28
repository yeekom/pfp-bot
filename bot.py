import discord
from discord import app_commands
import os
from flask import Flask
import threading

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot is ready! Logged in as {bot.user}")

@tree.command(name="hello", description="Replies with a hello message!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! I'm alive and running on Render!")

threading.Thread(target=run_web).start()  # Start web server in a separate thread
bot.run(TOKEN)
