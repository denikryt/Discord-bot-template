import os
import discord
from flask import Flask, jsonify, request
from threading import Thread
from discord import Intents, Client, Message, Forbidden, MessageType
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN_DISCORD = os.environ.get('TOKEN_DISCORD')

DISCORD_CHANNEL_ID_DOOR_EVENTS = os.environ.get('DISCORD_CHANNEL_ID_DOOR_EVENTS')

# -----------Flask app Configuration -----------
app = Flask('')

# ----------- Discord Bot Configuration -----------
intents = Intents.default()
intents.message_content = True 
discord_client = Client(intents=intents)

#------------------------------------------
def send_new_message_to_discord_async():

    text = ''

    discord_channel = discord_client.get_channel(int(DISCORD_CHANNEL_ID_DOOR_EVENTS))

    if discord_channel:
        # Ожидаем отправки сообщения и получаем объект отправленного сообщения
        discord_channel.send(text)
        print(f'New message sent to discord')
        
#------------------------------------------
@app.route('/')
def home():
    return 'Both bots are running'

def run():
    app.run(host="0.0.0.0", port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Keep the server alive and run both bots
keep_alive()
discord_client.run(TOKEN_DISCORD)
