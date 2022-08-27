if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/VysakhTG/ForwardBot.git /ForwardBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ForwardBot
fi
cd /ForwardBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
