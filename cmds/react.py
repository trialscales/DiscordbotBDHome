from discord.ext import commands 
from core.classes import Cog_Extension
import discord
import random
import json

# 打開token.json，讀取裡面的token
with open('setting.json', "r", encoding = "utf8") as file:
    data = json.load(file)


class React(Cog_Extension):

    # 在(data['pic'])庫里隨機發圖片
    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(data['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    # 在(data['url_pic'])庫里隨機發連結
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(data['url_pic'])
        await ctx.send(random_pic)

# 載入cog中
async def setup(bot):
    await bot.add_cog(React(bot))