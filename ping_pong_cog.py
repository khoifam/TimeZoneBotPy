from discord.ext import commands

class PingPongCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("PingPongCog initialized")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def bing(self, ctx):
        await ctx.send("bong")

    @commands.command()
    async def ding(self, ctx):
        await ctx.send("dong")

    @commands.command()
    async def ching(self, ctx):
        await ctx.send("bruh")

async def setup(bot):
    await bot.add_cog(PingPongCog(bot))
