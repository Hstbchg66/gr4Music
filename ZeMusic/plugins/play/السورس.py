import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["𝗚𝗥𝟰","‹ 𝗚𝗥𝟰 ›","𝗚𝗥𝟰","𝗚𝗥𝟰", "𝗚𝗥𝟰"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1564e5bd7d494767e0bfa.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [𝗚𝗥𝟰](https://t.me/WLT2_TEAM_CHAT)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/Mohamed_Was_Here"), 
                    
                
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/WLT2_TEAM_CHAT"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ القناة ›", url=f"https://t.me/for_Mohamed_Was_Here"),
                
        ],

            ]

        ),

    )

