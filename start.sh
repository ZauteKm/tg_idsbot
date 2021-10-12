echo "Cloning Repo...."
git clone https://github.com/ZauteKm/tg_idsbot.git /tg_idsbot
cd /tg_idsbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
