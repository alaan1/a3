import os

from telethon import Button, events

from DRAGON import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/ad1daabac933ff9e49316.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@DRACULA_2023"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@DRAGON.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/DRACULA_2023/670")]]
    await DRAGON.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
