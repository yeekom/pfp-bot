import discord
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Get the token from environment variables

intents = discord.Intents.default()
bot = discord.Client(intents=intents)  # Create the bot client
tree = app_commands.CommandTree(bot)  # Create a command tree for slash commands

@bot.event
async def on_ready():
    await tree.sync()  # Sync slash commands with Discord
    print(f"Bot is ready! Logged in as {bot.user}")

@tree.command(name="hello", description="Replies with a hello message!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! I'm alive and running on Render!")

bot.run(TOKEN)
