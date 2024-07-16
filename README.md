<h1 align="center">TimeZoneBot.py</h1>

<p align="center"><i>A discord bot that displays time zones as text channel's topic.</i></p>

# How to run
1. Build the Dockerfile to a docker image
```sh
sudo docker build . -t khoifam/timezonebotpy --no-cache
```
2. Run the docker image with your discord bot token with the environment variable "DISCORD_BOT_TOKEN"  
```sh
sudo docker run -e DISCORD_BOT_TOKEN=your_token -e MONGODB_CONNSTRING="mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.12" --name timezonebotpy --network="host" -dt khoifam/timezonebotpy
```
3. Inspect the bot's logs:
```sh
sudo docker logs -f timezonebotpy   
```