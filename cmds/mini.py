from discord.ext import commands 
# 導入core資料夾中的自寫模組
from core.classes import Cog_Extension

# 繼承Cog_Extension的self.bot物件
class Main(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot
    
    # 前綴指令
    @commands.command()
    async def Hello(self, ctx):
        await ctx.send("Hello, world!")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send("Hello, world!")

    # 指令 - ping
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}[ms]')
    
    # 指令 - HI
    @commands.command()
    async def hi(ctx):
        await ctx.send(f"!Hi <@{ctx.author.id}>")

# 載入cog中
async def setup(bot):
    await bot.add_cog(Main(bot))