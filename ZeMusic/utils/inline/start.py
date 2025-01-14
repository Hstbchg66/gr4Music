from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𖣂 ضيفني 𖣂", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𖣂 الدعم 𖣂", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𖣂 ضيفني 𖣂",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𖣂 **الـاوامر** 𖣂", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𖣂 👤 مطور البوت 𖣂", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𖣂 الدعم 𖣂", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="𖣂 جروب المطور 𖣂", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="𖣂 جروب السورس السورس 𖣂", url=f"https://t.me/WLT2_TEAM_CHAT"),
        ],
    ]
    return buttons
