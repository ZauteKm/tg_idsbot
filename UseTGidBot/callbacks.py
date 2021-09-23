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
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from Config import Config
from Data import Data


# Callbacks
@Client.on_callback_query()
async def _calls(bot, callback_query):
	chat_id = callback_query.from_user.id
	message_id = callback_query.message.message_id
	# .lower() to test somethings..
	if callback_query.data.lower() == "home":
		user = await bot.get_me()
		mention = user["mention"]
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.START.format(
				callback_query.from_user.mention, mention, callback_query.from_user.id
			),
			reply_markup=InlineKeyboardMarkup(Data.buttons),
		)
	if callback_query.data.lower() == "about":
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.ABOUT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)

	if callback_query.data.lower() == "source":
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.SOURCE,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)
	if callback_query.data.lower() == "help":
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.HELP,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_button),
		)
		""" More Plans """
