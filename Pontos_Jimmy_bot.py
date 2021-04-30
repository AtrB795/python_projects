import os.path
import pickle
from datetime import date
import discord
import arrow
import discord
import pandas as pd
import requests
from discord.ext import commands
from discord.utils import get
from ics import Calendar
# from blinkt import set_pixel, set_brightness, show, clear
from prsaw import RandomStuff

data_dict_of_message_authors_file = "data_dict_of_message_authors"

if os.path.exists(data_dict_of_message_authors_file):
    with open(data_dict_of_message_authors_file, "rb") as input_file:
        data_dict_of_message_authors = pickle.load(input_file)
else:
    data_dict_of_message_authors = {}
dataframe_of_message_authors = pd.DataFrame({'name': ['AtrB'], 'activity': [0]})
dataframe_of_message_authors.set_index("name", inplace=True)

first_date = 16

rs = RandomStuff(async_mode=True)
i = -1
url = 'https://esuli.kossuthgyakorlo.unideb.hu/calendar/export_execute.php?userid=2802&authtoken=f80e6c4208472c2b1140c6c91f393dc367f66601&preset_what=all&preset_time=monthnow'
client = commands.Bot(command_prefix='+')
client2 = discord.Client()


def get_just_the_number(datum):
    stringed_date = str(datum)
    new_string = stringed_date[-2] + stringed_date[-1]
    return int(new_string)


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    global list_of_message_authors
    global data_dict_of_message_authors
    print(dataframe_of_message_authors)

    this_day = get_just_the_number(date.today())


days = this_day - first_date
if days == 0:
    message_authors_activity = data_dict_of_message_authors[message.author.name]
else:
    message_authors_activity = data_dict_of_message_authors[message.author.name] / days

try:
    dataframe_of_message_authors.loc[message.author.name].loc['activity'] = message_authors_activity[
        message.author.name]

dataframe_of_message_authors = dataframe_of_message_authors.append('name':message.author.name, '')


if client.user == message.author:
    return
if message.author.name not in data_dict_of_message_authors:
    data_dict_of_message_authors[message.author.name] = 1
else:
    data_dict_of_message_authors[message.author.name] += 1

dataframe_of_message_authors = dataframe_of_message_authors.append(
    {'name': message.author.name, 'activity': message_authors_activity}, ignore_index=True)

if message_authors_activity < 3:
    await message.channel.send(
        f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 1')
    role = get(message.author.guild.roles, name="próba")
    await message.author.add_roles(role)
if message_authors_activity == 5:
    await message.channel.send(
        f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 2')
    role = get(message.author.guild.roles, name="not_active")
    await message.author.add_roles(role)
if message_authors_activity == 30:
    await message.channel.send(
        f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 3')
    role = get(message.author.guild.roles, name="he_is_here")
    await message.author.add_roles(role)
if message_authors_activity == 40:
    await message.channel.send(
        f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 4')
    role = get(message.author.guild.roles, name="active")
    await message.author.add_roles(role)
if message_authors_activity == 150:
    await message.channel.send(
        f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: -1')
    role = get(message.author.guild.roles, name="spammer")
    await message.author.add_roles(role)

if message_authors_activity < 3:
    await message.author.remove_roles(get(message.author.guild.roles, name="not_active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="he_is_here"))
    await message.author.remove_roles(get(message.author.guild.roles, name="active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="spammer"))
if 30 > message_authors_activity >= 5:
    await message.author.remove_roles(get(message.author.guild.roles, name="próba"))
    await message.author.remove_roles(get(message.author.guild.roles, name="he_is_here"))
    await message.author.remove_roles(get(message.author.guild.roles, name="active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="spammer"))
if 40 > message_authors_activity >= 30:
    await message.author.remove_roles(get(message.author.guild.roles, name="próba"))
    await message.author.remove_roles(get(message.author.guild.roles, name="not_active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="spammer"))
if 150 > message_authors_activity >= 40:
    await message.author.remove_roles(get(message.author.guild.roles, name="próba"))
    await message.author.remove_roles(get(message.author.guild.roles, name="not_active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="he_is_here"))
    await message.author.remove_roles(get(message.author.guild.roles, name="spammer"))
if message_authors_activity >= 150:
    await message.author.remove_roles(get(message.author.guild.roles, name="próba"))
    await message.author.remove_roles(get(message.author.guild.roles, name="not_active"))
    await message.author.remove_roles(get(message.author.guild.roles, name="he_is_here"))
    await message.author.remove_roles(get(message.author.guild.roles, name="active"))

if message.content.startswith('mi_lesz_ekkor'):
    cal = Calendar(requests.get(url).text)
    datum = get_just_the_number(message.content)
    # message_channel = client.get_channel(821351000144609290)
    try:
        for event in cal.timeline.on(arrow.get(2021, 3, datum)):
            text = f'Esemény: {event.name}: \n{event.description}. Ekkor kezdődik: {event.begin}\n És ekkor fejeződik be: {event.end}'
            await message.channel.send(text)
    except ValueError:
        await message.channel.send('Ilyen nap Márciusban nincs sajna!')

if message.content.startswith('my_activity'):
    await message.channel.send(f'Ennyit fecsegsz a szerveren: {message_authors_activity} / nap ')

with open(data_dict_of_message_authors_file, 'wb') as output_file:
    pickle.dump(data_dict_of_message_authors, output_file)

if message.channel.id == 825019154045337660:
    # message_channel2 = client.get_channel(825019154045337660)
    response = await rs.get_ai_response(message.content)
    await message.channel.send(response)

# bot = commands.Bot(command_prefix='!')


client.run("ODA2OTYzMDY2Nzc5NDY3Nzk2.YBxE6w.rPwvxs08Mx4Lhs-XANQZjv_imb0")
