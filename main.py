from discord.ext import commands
import discord

#Bot prefix
client = commands.Bot(command_prefix="gry ")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Hi, my prefix is `gry`.")


client.run("ODQ3MTI4NzIxMzIwMzEyODQz.YK5kGg.wRExNqgGU8iRsRVQ-4diSzqmVWY")
