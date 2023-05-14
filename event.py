# 引用About讀取資料

from About import bot

@bot.event
async def on_message(message):
    # 判斷訊息內容是否為 Hello
    if message.content == "Hello":
        # 回覆 Hello, world!
        await message.channel.send("Hello, world!")

@bot.event
async def on_message(message):
    # 判斷訊息內容是否為 123
    if message.content == "123":
        # 回覆 Hello, world!
        await message.channel.send("Hello, 123!")