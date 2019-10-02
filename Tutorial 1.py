import discord
from discord.ext import commands

# Initialise Client
client = commands.Bot(command_prefix="?")  # Initialise client bot


@client.event
async def on_ready():
    # This will be called when the bot connects to the server
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    if message.content == "cookie":
        # responds with Cookie emoji when someone says "cookie"
        await message.channel.send(":cookie:")

client.run("token")  # Replace token with your bots token
