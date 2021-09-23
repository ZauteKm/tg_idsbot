# UseTGidBot

Telegram bot to give id of any user, group,bot, channels and even stickers.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/ZauteKm)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/ZauteKm)

---

[![GitHub forks](https://img.shields.io/github/forks/ZauteKm/UseTGidBot.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/ZauteKm/UseTGidBot/network/) [![GitHub stars](https://img.shields.io/github/stars/ZauteKm/UseTGidBot.svg?style=social&label=Star&maxAge=2592000)](https://github.com/ZauteKm/UseTGidBot/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/ZauteKm/UseTGidBot.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/ZauteKm/UseTGidBot/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ZauteKm/UseTGidBot/graphs/commit-activity)

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

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ZauteKm/UseTGidBot)

---

### Deploy in your VPS

```
git clone https://github.com/ZauteKm/UseTGidBot
cd UseTGidBot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

---
