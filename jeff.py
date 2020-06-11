import discord
from yahoo_fin import stock_info as stk
from zalgo_text import zalgo


TOKE = ''
run = False
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if('$stock' in message.content):
        str = message.content.split()
        await message.channel.send(str[1] + " price in USD:")
        await message.channel.send(stk.get_live_price(str[1]))
    elif('jeff' in message.content):
        mystr = zalgo.zalgo().zalgofy(message.content)
        await message.channel.send(mystr)
    elif('$$' in message.content):
        channel = message.channel
        messages = await channel.history().flatten()
        if(len(message.content) > 3):
            messagestr = messages[int(message.content[3])].content
        else:
            messagestr = messages[1].content
        newstr = ""
        count = 1
        for i in messagestr:
            if(count):
                newstr += i
                count -= 1
            else:
                newstr += i.upper()
                count += 1
        await message.channel.send(newstr)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---')

client.run(TOKE)
