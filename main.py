from discord.ext import commands
import discord

#Bot prefix
client = commands.Bot(command_prefix="gry ")
client.remove_command(help)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and message.mention_everyone is False:
        prefix= get_prefix
        await message.channel.send(f"My prefix is {client.command_prefix}")

     await client.process_commands(message)

@client.event
async def on_message(message):
    if "gryphon" in message:
        await message.channel.send("Test successful!")

client.run("ODQ3MTI4NzIxMzIwMzEyODQz.YK5kGg.wRExNqgGU8iRsRVQ-4diSzqmVWY")
