<b>Telethon Targeted Auto-Responder</b>

This repository contains a personal Telethon-based userbot prototype.
The bot monitors a specific Telegram chat and automatically sends an instant response whenever a predefined user sends a message.
It serves as a lightweight example of:

Targeted message detection

Filtering by chat and sender

Real-time auto-responses

Basic event handling with Telethon

Features

🔍 Listens to one specific chat

🎯 Reacts only to one predefined user

⚡ Sends an instant automated response

🧩 Minimal, clean implementation

🛠️ Built entirely with Telethon

Requirements

Python 3.9+

Telethon

Telegram API ID & API Hash

Install dependencies:

pip install telethon

How It Works

The userbot registers an event listener on incoming messages.
Whenever the target user sends a message in the chosen chat, the bot immediately replies with your predefined response.

This project is meant to be a simple, personal reference for anyone exploring:

How userbots work

Telethon event listeners

Filtering by chat ID and user ID

Automated message handling

Disclaimer

This project is for personal and educational use only.
Use responsibly and in accordance with Telegram's Terms of Service.
