from pontos_jimmy_oop import Pontos_Jimmy
from discord.ext import commands

client = Pontos_Jimmy()


@client.event
async def on_ready():
    client.on_ready()

@client.event
async def on_message(message):
    client.on_message(message)

