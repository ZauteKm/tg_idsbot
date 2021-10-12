#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from bot import app
from config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hi {}. \n\nWelcome to {} \n\nUsing this bot you can check id of any group, user, bot, channel and even stickers."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\n▷ Made by ❤️ @ZauteKm"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @ZauteKm"
    START += "\n\nP.S ~ Your ID is `{}`"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an open source ID bot by @ZauteKm \n\nSupport Chat: [Join Now](https://t.me/iZaute/5) \n\nFramework: [Pyrogram](docs.pyrogram.org) \n\nLanguage: [Python](www.python.org) \n\nDeveloper: [Zaute Km](https://t.me/iZaute/6)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\n▷ Please Subscribe ❤️ @ZauteKm"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Help Message
    HELP = "**Help & Features** \n\n1) Send any message to get your ID. \n2) Forward any message from any user/bot/channel or anonymous admins to get ID. \n3) Send any sticker to get sticker id. \n4) Use Inline Mode to send your ID in any chat. \n5) Add in group / channel to get ID. \n6) Use /id command: \n- in private: To get ID through username \n- in group/channel: To get ID of that chat. \n\nMizo Version [Hmet Rawh](https://telegra.ph/Telegram-ID-Bot-Hmandan-03-16). \n\n▷Please Subscribe ❤️ @ZauteKm"

    # Source Code Message
    SOURCE = '**Telegram Id Bot Source** \n\n• @tg_idsbot. \n\n<b>Source Code</b> [Click me](https://github.com/ZauteKm/tg_idsbot)'

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🖲️ Help", callback_data="help"),
            InlineKeyboardButton("About 🤖", callback_data="about"),
        ],
        [InlineKeyboardButton("👥 Group", url="https://t.me/iZaute/5"),
        InlineKeyboardButton("Channel 📢", url="https://t.me/iZaute/6")
        ],
        [InlineKeyboardButton("🔰 Source Code -GitHub 🔰", callback_data="source")],
    ]
