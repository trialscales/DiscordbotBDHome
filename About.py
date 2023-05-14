# 引用包
## 導入commands指令模組
from discord.ext import commands 
## 導入Discord.py模組
import discord
import json
import os

# 添加前綴字符
## intents是要求機器人的權限
intents = discord.Intents.default()
intents.members = True
## command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix='!')
## client是跟discord連接，intents是要求機器人的權限
client = discord.Client(intents = intents)

#自訂help
@bot.event
async def on_ready():
    bot.remove_command("help")

# 打開token.json，讀取裡面的token
with open('setting.json', "r", encoding = "utf8") as file:
    data = json.load(file)
    
# 添加事件 表示bot已經成功啟動 (終端機)
@bot.event
async def on_ready():
    print("Bot in ready")

# 添加事件 表示bot已經連接到Discord伺服器 (終端機)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# 添加事件 表示bot已經成功啟動 (終端機)
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

#執行載入(load)
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

#卸載(unload)
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Un - Loaded {extension} done.")

#重新載入(reload)
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Re - Loaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    # 迴圈做判斷，讀取資料夾
    for filename in os.listdir("./cmds"):
        #這裡只讀取py文件
        if filename.endswith(".py"):
            #導入用bot刪除後三個字
            bot.load_extension(F"cmds.{filename[:-3]}")

# keyword
if __name__ == "__nain__":
    bot.run(data["token"])

bot.run(data["token"])