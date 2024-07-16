from time_zone_channel_manager import TimeZoneChannelManager
from discord.ext import commands
import pytz
from datetime import datetime

class TimeZoneUpdater():
    def __init__(self, channel_manager: TimeZoneChannelManager, bot: commands.Bot) -> None:
        self.channel_manager = channel_manager
        self.bot = bot
        self.time_zones = ["Asia/Ho_Chi_Minh", "Australia/Sydney", "America/Los_Angeles", "America/New_York"]
        
    def construct_time_str(self) -> str:
        time_strings = []
        for time_zone in self.time_zones:
            tz_cur_time = datetime.now(pytz.timezone(time_zone)).time()
            time_str = tz_cur_time.strftime("%I:%M %p")
            time_strings.append(time_str)
        
        output = "VN: " + time_strings[0] + " ---- AUS: " + time_strings[1] + " ---- West: " \
            + time_strings[2] + " ---- East: " + time_strings[3]

        print("TimeZoneUpdater:", output)
        return output
    
    async def update(self):
        topic_str = self.construct_time_str()

        for id in self.channel_manager.get_text_channel_ids():
            text_channel = self.bot.get_channel(id)
            if text_channel != None:
                print("TimeZoneUpdater:", text_channel.name, text_channel.id)
                await text_channel.edit(topic=topic_str)
            else:
                self.channel_manager.prune_id_from_db(id)