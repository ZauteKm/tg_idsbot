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
from pyrogram import Client, filters


# Forwarded
@Client.on_message(filters.private & filters.forwarded)
async def forwarded(bot, msg):
    if msg.forward_from:
        text = "Forward detected! \n\n"
        if msg.forward_from["is_bot"]:
            text += "**Bot**"
        else:
            text += "**User**"
        text += f'\n{msg.forward_from["first_name"]} \n'
        if msg.forward_from["username"]:
            text += f'@{msg.forward_from["username"]} \nID : `{msg.forward_from["id"]}`'
        else:
            text += f'ID : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"Forward Detected. \n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "**Channel**"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "**Group**"
            text += f'\n{msg.forward_from_chat["title"]} \n'
            if msg.forward_from_chat["username"]:
                text += f'@{msg.forward_from_chat["username"]} \n'
                text += f'ID : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'ID : `{msg.forward_from_chat["id"]}`'
            await msg.reply(text, quote=True)
