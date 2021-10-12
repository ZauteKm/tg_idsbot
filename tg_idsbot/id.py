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
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied


# ID through Username
@Client.on_message(filters.command("id"))
async def id(bot, msg):
	if not msg.chat.type == "private":
		await msg.reply(f"This {msg.chat.type}'s ID is `{msg.chat.id}`")
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Your Telegram ID is: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					check = uname[1:]
				else:
					await msg.reply("Username should start with '@'", quote=True)
					return
				try:
					user = await bot.get_users(check)
					name = user["first_name"]
				except:
					user = await bot.get_chat(check)
					name = user["title"]
				if len(name) <= 20:
					pass
				elif user["is_bot"]:
					name = "This Bot"
				else:
					name = "This User"
				id = user["id"]
				await msg.reply(f"{name}'s id is `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("This username is not occupied by anyone", quote=True)
