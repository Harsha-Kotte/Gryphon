from discord.ext import commands
import discord

#Bot prefix
client = commands.Bot(command_prefix="gry ")
client.remove_command(help)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

async def on_mention(self,message):
    user_id = self.bot.user.id
    if message.content in (f"<@{user_id}>", f"<@!{user_id}>"):
        await message.reply("Myself Gryphon and my prefix is `gry `.\nYou can start up with `gry help`.")


client.run("ODQ3MTI4NzIxMzIwMzEyODQz.YK5kGg.wRExNqgGU8iRsRVQ-4diSzqmVWY")
