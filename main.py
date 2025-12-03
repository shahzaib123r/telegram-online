from telethon import TelegramClient
import asyncio

# ==== CHANGE THESE ====
api_id = 123456            # <-- yahan apna API ID likho
api_hash = "YOUR_API_HASH" # <-- yahan apna API Hash likho
session_name = "online_session"
# =======================

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    print("Connecting…")
    await client.connect()

    if not await client.is_user_authorized():
        print("First time login… enter the code sent to your Telegram.")
        await client.send_code_request(phone='')
    
    print("✨ Telegram Online Bot Started (24/7)…")

    # Infinite loop that keeps account online
    while True:
        await client.send_read_acknowledge("me")   # keeps session alive
        await asyncio.sleep(20)                    # ping every 20 sec

with client:
    client.loop.run_until_complete(main())
