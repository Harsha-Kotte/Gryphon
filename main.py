from discord.ext import commands
from discord.ui import Button
import discord

#Bot prefix
client = commands.Bot(command_prefix="gry ")
client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Hi, my prefix is `gry`.")

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Gryphon configurations", description="This will help you know the features of the bot.", color="#03fcd3")
    em.set_footer(text="Click the buttons below to explore the ctaegory you want...")
    await ctx.send(embed=em)
    
client.run("ODQ3MTI4NzIxMzIwMzEyODQz.YK5kGg.wRExNqgGU8iRsRVQ-4diSzqmVWY")
