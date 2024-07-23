from discord import TextChannel
from pymongo import MongoClient

class TimeZoneChannelManager():
    def __init__(self) -> None:
        self.text_channel_ids_table = MongoClient("timezonebotpy-db", 27017)["timezonebotpy"]["textchannels"]

    def get_text_channel_ids(self) -> set:
        ids = set()
        for row in self.text_channel_ids_table.find():
            ids.add(row["id"])
        return ids

    def text_channel_add(self, text_channel: TextChannel):
        if self.text_channel_ids_table.find_one({"id" : text_channel.id}) != None: 
            return "The bot is already running for this text channel."
        else:
            self.text_channel_ids_table.insert_one({"id" : text_channel.id})
            return "Time zones are now being updated every 10 minutes for this text channel!"

    def text_channel_info(self, text_channel: TextChannel) -> str:
        print("TimeZoneChannelManager:", text_channel.id, text_channel.name)
        if self.text_channel_ids_table.find_one({"id" : text_channel.id}) != None: 
            return "The bot is already running for this text channel."
        else:
            return "The bot is not activated for this text channel. Type \"addbingbong\" to activate."
        
    def text_channel_remove(self, text_channel: TextChannel):
        if self.text_channel_ids_table.find_one({"id" : text_channel.id}) != None:
            self.text_channel_ids_table.delete_one({"id" : text_channel.id})
            return "This bot is now deactivated for this text channel."
        else:
            return "This bot has already been deactivated for this text channel."
        
    def prune_id_from_db(self, id: int):
        self.text_channel_ids_table.delete_many({"id" : id})