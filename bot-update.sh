echo "Killing Botto"
screen -S Status-Botto -X quit
echo "Updating Botto"
git pull
echo "Starting Botto"
screen -dmS Status-Botto bot.py