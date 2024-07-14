from discord.ext import commands, tasks
from time_zone_channel_manager import TimeZoneChannelManager
from time_zone_updater import TimeZoneUpdater

class TimeZoneCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel_manager = TimeZoneChannelManager()
        self.time_zone_updater = TimeZoneUpdater(self.channel_manager, self.bot)
        self.updater_task.start()
        print("TimeZoneCog initialized")

    @commands.command()
    async def addbingbong(self, ctx: commands.Context):
        resp = self.channel_manager.text_channel_add(ctx.channel)
        await ctx.send(resp)

    @commands.command()
    async def bingbong(self, ctx: commands.Context):
        # print(ctx.channel.id)
        resp = self.channel_manager.text_channel_info(ctx.channel)
        await ctx.send(resp)

    @commands.command()
    async def removebingbong(self, ctx: commands.Context):
        resp = self.channel_manager.text_channel_remove(ctx.channel)
        await ctx.send(resp)

    def cog_unload(self):
        self.updater_task.cancel()

    @tasks.loop(seconds=61.0)
    async def updater_task(self):
        print("Update")
        await self.time_zone_updater.update()

    @updater_task.before_loop
    async def before_updater_task(self):
        print("Updater waiting...")
        await self.bot.wait_until_ready()

async def setup(bot: commands.Bot):
    await bot.add_cog(TimeZoneCog(bot))