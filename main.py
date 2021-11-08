from discord.ext import commands
import discord

#Bot prefix
client = commands.Bot(command_prefix="?")
client.remove_command(help)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("vdYrHKNBuRr9ctghKsffR6zFDCXbuGAC")
