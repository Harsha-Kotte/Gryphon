from discord.ext import commands
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("vdYrHKNBuRr9ctghKsffR6zFDCXbuGAC")
