import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import config

DISCORD_BOT_TOKEN = config.DISCORD_BOT_TOKEN
OPENAI_EMAIL = config.OPENAI_EMAIL
OPENAI_PASSWORD = config.OPENAI_PASSWORD

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)
prefix = "/"

async def on_ready():
    channel_id = 123456  # Replace with your channel ID
    channel = client.get_channel(channel_id)
    message = "Hello, this is a test message from the Beluga!"
    await channel.send(message)

@client.event
async def handle_command(message, command):
    channel_id = 123456  # Replace with your channel ID
    channel = client.get_channel(channel_id)

    if command == "ping":
        await channel.send("pong")
    elif command.startswith("login "):
        email, password = command.split()[1:]
        initial_message, session_cookies = login(email, password)
        session = requests.session()
        session.cookies.update(session_cookies)
        message = f":bell: {initial_message}"
        await channel.send(message)
    elif command.startswith("send "):
        message_text = command.split(maxsplit=1)[1]
        response, is_thinking = send_message(message_text, session)
        if is_thinking:
            message = f":hourglass: {response}"
        else:
            message = f":yellow_circle: {response}"
        await channel.send(message)
    elif command == "help":
        help_message = "Available commands:\n"
        help_message += f"`{prefix}ping`: Test the bot's responsiveness\n"
        help_message += f"`{prefix}login <email> <password>`: Log in to the OpenAI chat website\n"
        help_message += f"`{prefix}send <message>`: Send a message to the OpenAI chat website\n"
        help_message += f"`{prefix}help`: List available commands\n"
        help_message += f"`{prefix}about`: Display information about the bot\n"
        await channel.send(help_message)
    elif command == "about":
        message = ":cat: I am Beluga Cat, an intelligent chatbot powered by OpenAI!"
        await channel.send(message)
    else:
        message = f":x: Unknown command `{prefix}{command}`"
        await channel.send(message)

def login(email, password):
    login_page = requests.get("https://chat.openai.com/login")
    soup = BeautifulSoup(login_page.content, "html.parser")
    csrf_token = soup.find("input", {"name": "_csrf_token"})["value"]
    login_data = {
        "_csrf_token": csrf_token,
        "email": email,
        "password": password,
    }
    login_request = requests.post(
        "https://chat.openai.com/login", data=login_data
    )
    chat_page = requests.get("https://chat.openai.com/chat")
    soup = BeautifulSoup(chat_page.content, "html.parser")
    initial_message = soup.find("div", {"class": "message"})["data-message"]
    return initial_message, login_request.cookies

def send_message(message, session):
    chat_data = {"message": message}
    chat_request = session.post(
        "https://chat.openai.com/chat", data=chat_data
    )
    soup = BeautifulSoup(chat_request.content, "html.parser")
    response_divs = soup.find_all("div", {"class": "message"})
    response = response_divs[-1]["data-message"]
    is_thinking = response_divs[-1].get("data-thinking", False)
    return response, is_thinking

@client.event
async def on_message(message):
    if not message.content.startswith(prefix):
        return

    command = message.content[len(prefix):].strip()
    await handle_command(message, command)

client.run(DISCORD_BOT_TOKEN)

