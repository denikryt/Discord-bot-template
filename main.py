import os
import discord
from discord import Intents, Client
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Retrieve the bot token and channel ID from environment variables
DOOR_BOT_TOKEN = os.environ.get('DOOR_BOT_TOKEN')
DISCORD_CHANNEL_ID_DOOR_EVENTS = os.environ.get('DISCORD_CHANNEL_ID_DOOR_EVENTS')

# Discord Bot Configuration
intents = Intents.default()
intents.message_content = True 
discord_client = Client(intents=intents)

# Function to send a message to the specified Discord channel
async def send_new_message_to_discord():
    text = 'hello'  # The message to send
    discord_channel = discord_client.get_channel(int(DISCORD_CHANNEL_ID_DOOR_EVENTS))

    if discord_channel:
        await discord_channel.send(text)
        print(f'New message sent to discord')

# Event handler when the bot is ready
@discord_client.event
async def on_ready():
    print(f'Bot has logged in as {discord_client.user}')
    await send_new_message_to_discord()  # Send the message when the bot is ready

# Run the bot
discord_client.run(DOOR_BOT_TOKEN)
