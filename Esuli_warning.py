import discord
from discord.ext import commands
client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    print("Bot is ready!")
@client.command()
async def hello(ctx):
    await ctx.send("hi")
client.run("ODE5MjQxMzIxODA1NjQzNzg4.YEjv7w.tDYlxUrf9AMVkkzHn4JiyCnECCg")