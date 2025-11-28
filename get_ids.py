import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# --- Load .env ---
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "get_ids_session")

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

print("\n>>> Starting... If first time, Telegram will send you a login code.\n")

@client.on(events.NewMessage(pattern=r'^/me$'))
async def handler_me(event):
    sender = await event.get_sender()
    uid = sender.id
    await event.reply(f"Your User ID is: `{uid}`")
    print(f"[INFO] User ID: {uid}")

@client.on(events.NewMessage(pattern=r'^/chat$'))
async def handler_chat(event):
    chat_id = event.chat_id
    await event.reply(f"Chat ID: `{chat_id}`")
    print(f"[INFO] Chat ID: {chat_id}")

async def main():
    print("Bot is running.\n"
          "• Send /me to ANY chat to get the sender's user id.\n"
          "• Send /chat inside a group to get the group id.\n")

# --- Start client manually (Python 3.14 fix) ---
client.start()
client.loop.run_until_complete(main())
client.run_until_disconnected()
