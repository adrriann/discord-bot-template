import discord
from discord import Intents
from discord.ext import commands

intents = Intents.default()
client = commands.Bot(command_prefix='!', Intents=Intents.default.all())

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send('ong')


client.run('your token here')
