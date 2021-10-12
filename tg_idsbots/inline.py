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
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


# Inline Mode
@Client.on_inline_query()
async def answer(bot, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"Your Telegram ID is {inline_query.from_user.id}",
				input_message_content=InputTextMessageContent(
					f"My Telegram ID is `{inline_query.from_user.id}`"
				),
				description="Tap to send your ID to current chat",
				thumb_url="https://telegra.ph/file/a894f9a8f50c2a063f06f.jpg",
			)
		],
		cache_time=1,
	)
