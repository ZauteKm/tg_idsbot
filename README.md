# idsbot [telegram]

Telegram bot to give id of any user, group,bot, channels and even stickers.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/ZauteKm)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/ZauteKm)

---

[![GitHub forks](https://img.shields.io/github/forks/ZauteKm/tg_idsbot.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/ZauteKm/tg_idsbot/network/) [![GitHub stars](https://img.shields.io/github/stars/ZauteKm/tg_idsbot.svg?style=social&label=Star&maxAge=2592000)](https://github.com/ZauteKm/tg_idsbot/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/ZauteKm/tg_idsbot.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/ZauteKm/tg_idsbot/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ZauteKm/tg_idsbot/graphs/commit-activity)

---

## Features

1. Telegram bot to give id of any user, group,bot, channels.
2. Support for using in groups and channels
3. Support for Inline Mode
4. Also support to het id by Forwarding any message to the bot from users, bots, channels and even anonymous admins.
5. Get id from usernames too.
6. Specify owner's account to get help or something.

To-Do

1. Database for stats
2. Add more group features.
3. Add more inline features

---

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@UseTGZKBot](https://t.me/usetgzkbot)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@UseTGzKbot](https://t.me/usetgzkbot)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)

#### Optional Vars

> (fill both or neither)

- `OWNER_ID` - Get it from [@UseTGidBot](https://t.me/UseTGidBot) by sending /id to it.
- `OWNER_NAME` - Your Name (to be shown as owner in bot)

---

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ZauteKm/tg_idsbot)

---

### Deploy in your VPS

```
git clone https://github.com/ZauteKm/tg_idsbot
cd tg_idsbot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

---

## License

```
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
```

---
