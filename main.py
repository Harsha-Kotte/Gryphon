from discord.ext import commands
import discord

#Bot prefix
client = commands.Bot(command_prefix="gry ")
client.remove_command(help)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_mention(message):
    if client.user.mentioned_in(message):
        channel = message.channel 
        await channel.send("Myself Gryphon and my prefix is `gry `.\nYou can start up with `gry help`.")


client.run("ODQ3MTI4NzIxMzIwMzEyODQz.YK5kGg.wRExNqgGU8iRsRVQ-4diSzqmVWY")
