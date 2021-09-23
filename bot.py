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
import logging
from pyrogram import Client, idle
from Config import Config


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    "UseTGidBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="UseTGidBot"),
)


# Run Bot
if __name__ == "__main__":
    app.start()  # Not using run as wanna print
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")
    idle()
    app.stop()
    print("Bot stopped. Subscribe @TGBotsProJect!")
