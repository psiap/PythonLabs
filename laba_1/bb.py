import asyncio
import random
import time

import socks
from telethon.sync import TelegramClient
from telethon.tl import functions


async def main():
    for i in array_clien:
        for j in await i.get_dialogs():
            print(j)


    time.sleep(500)

def as_g():
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    loop.close()
    print(f"Время работы: {time.time() - start_time}")

as_g()
