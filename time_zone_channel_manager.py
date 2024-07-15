from discord import TextChannel
from asyncio import Lock

class TimeZoneChannelManager():
    def __init__(self) -> None:
        self.text_channel_ids = set()
        self.lock = Lock()

    async def get_text_channel_ids(self) -> set:
        async with self.lock:
            return self.text_channel_ids.copy()

    async def text_channel_add(self, text_channel: TextChannel):
        if text_channel.id in self.text_channel_ids: 
            return "The bot is already running for this text channel."
        else:
            async with self.lock:
                self.text_channel_ids.add(text_channel.id)
            return "Time zones are now being updated every 10 minutes for this text channel!"

    def text_channel_info(self, text_channel: TextChannel) -> str:
        print(text_channel.id, text_channel.name)
        if text_channel.id in self.text_channel_ids: 
            return "The bot is already running for this text channel."
        else:
            return "The bot is not activated for this text channel. Type \"addbingbong\" to activate."
        
    async def text_channel_remove(self, text_channel: TextChannel):
        if text_channel.id in self.text_channel_ids:
            async with self.lock:
                self.text_channel_ids.remove(text_channel.id)
            return "This bot is now deactivated for this text channel."
        else:
            return "This bot has already been deactivated for this text channel."