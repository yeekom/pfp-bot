import discord
from discord.ext import commands
import os
from flask import Flask
import threading

app = Flask(__name__)

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@app.route('/')
def home():
    return "Bot is alive!"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    activity = discord.Game(name="silly yeekom game 3000")  
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await bot.tree.sync()
  
@discord.app_commands.allowed_installs(guilds=True, users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="ping", description="pong")
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.user.send("pong")
    await interaction.response.send_message('pong')
    
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
            except discord.NotFound:
                pass  
            except discord.Forbidden:
                pass  
        else:
            pass  

    await bot.process_commands(message)

def run_bot():
    bot.run(os.getenv('DISCORD_TOKEN'))

def start():
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    run_bot()

if __name__ == "__main__":
    start()
