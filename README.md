<h1 align="center">TimeZoneBot.py</h1>

<p align="center"><i>A discord bot that displays time zones as text channel's topic.</i></p>

# How to run
1. Build the Dockerfile to a docker image
```sh
docker build . -t khoifam/timezonebotpy --no-cache
```
2. Run the docker image with your discord bot token with the environment variable "DISCORD_BOT_TOKEN"  
```sh
docker run -e DISCORD_BOT_TOKEN=your_token_ -d khoifam/timezonebotpy
```