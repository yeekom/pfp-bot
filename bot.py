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

@discord.app_commands.allowed_installs(guilds=False, users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@tree.command(name="hello", description="Replies with a hello message!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("pong", ephemeral=True)
    await interaction.user.send("pong")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        if message.content.isdigit():
            user_id = int(message.content)
            try:
                user = await bot.fetch_user(user_id)
 
                pfp_url = user.avatar.url  
                response = f"{pfp_url}"
 
                await message.channel.send(response)

threading.Thread(target=run_web).start() 
bot.run(TOKEN)
