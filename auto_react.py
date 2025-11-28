import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from datetime import datetime

# Load .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
TARGET_CHAT_IDS = int(os.getenv("TARGET_CHAT_IDS"))
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID"))
TARGET_REACTION = os.getenv("TARGET_REACTION").strip()

client = TelegramClient("auto_react_session", API_ID, API_HASH)
clear = lambda: os.system('cls')

LOG_FILE = "reactions.log"


def log_reaction(message_id):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now()} | Chat: {TARGET_CHAT_IDS} | "
            f"User: {TARGET_USER_ID} | Message: {message_id} | Reaction: {TARGET_REACTION}\n"
        )


async def run_bot():

    @client.on(events.NewMessage(chats=TARGET_CHAT_IDS))
    async def handler(event):
        sender = await event.get_sender()

        if sender.id == TARGET_USER_ID:
            try:
                await client(SendReactionRequest(
                    peer=TARGET_CHAT_IDS,
                    msg_id=event.message.id,
                    reaction=[ReactionEmoji(emoticon=TARGET_REACTION)]
                ))
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Reacted to message {event.message.id}")
                log_reaction(event.message.id)

            except Exception as e:
                print(f"[ERROR] {e}")

        # skip other users silently

    await client.start()
    clear()
    print("Tot Farangi Roshan...")
    await client.run_until_disconnected()


# Auto-restart loop
while True:
    try:
        asyncio.run(run_bot())
    except Exception as e:
        print(f"[FATAL] Bot crashed: {e}")
        print("Restarting in 5 seconds...\n")
        asyncio.sleep(5)
