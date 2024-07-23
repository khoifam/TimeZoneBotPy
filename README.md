<h1 align="center">TimeZoneBot.py</h1>

<p align="center"><i>A discord bot that displays time zones as text channel's topic.</i></p>

# How to run
Warning: To run this bot, you have to shutdown your local MongoDB `mongod` process by doing:
```sh
sudo systemctl stop mongod
```
1. Export YOUR discord bot token
```sh
export DISCORD_BOT_TOKEN=your_token
```
2. Run the docker compose file  
```sh
sudo docker compose up -d
```
3. Inspect the bot's logs:
```sh
sudo docker logs -f timezonebotpy-bot
```
4. Access the containerized database:
```sh
sudo docker exec -it timezonebotpy-db sh
```
```sh
mongosh
```