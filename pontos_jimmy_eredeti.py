import discord
import os.path
from discord.ext import commands, tasks
from datetime import date
import requests
from ics import Calendar
from discord.utils import get
import arrow
from blinkt import set_pixel, set_brightness, show, clear, set_all
import time
import colorsys
import pickle
from prsaw import RandomStuff






data_dict_of_message_authors_file = "data_dict_of_message_authors"

if os.path.exists(data_dict_of_message_authors_file):
    with open(data_dict_of_message_authors_file, "rb") as input_file:
        data_dict_of_message_authors = pickle.load(input_file)
else:
    data_dict_of_message_authors = {}


first_date = 6






set_brightness(1)
i = 0
rs = RandomStuff(async_mode = True)
url = 'https://esuli.kossuthgyakorlo.unideb.hu/calendar/export_execute.php?userid=2802&authtoken=f80e6c4208472c2b1140c6c91f393dc367f66601&preset_what=all&preset_time=monthnow'
cal = Calendar(requests.get(url).text)
client = commands.Bot(command_prefix='+')
client2 = discord.Client()
def get_just_the_number (datum):
    stringed_date = str(datum)
    new_string = stringed_date[-2] + stringed_date[-1]
    return int(new_string)#
@client.event
async def on_ready():
    print("Bot is ready!")
    print(client2.get_all_members())

@client.event
async def on_message(message):
    global i
    global first_date
    global data_dict_of_message_authors
    global list_of_message_authors


    if client.user == message.author:
        return
    if message.author.name not in data_dict_of_message_authors:
        data_dict_of_message_authors[message.author.name] = 1
    else:
        data_dict_of_message_authors[message.author.name] += 1


    this_day = date.today().day
    days = this_day - first_date
    if days == 0:
        message_authors_activity = data_dict_of_message_authors[message.author.name]
    else:
        message_authors_activity = data_dict_of_message_authors[message.author.name] / days

    print([message.author.name, message_authors_activity])

    if message_authors_activity == 3:
        await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 1')
#       role = get(message.author.guild.roles, name="próba")
#       await message.author.add_roles(role)
    if message_authors_activity == 10:
        await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 2')
#       role = get(message.author.guild.roles, name="not_active")
#       await message.author.add_roles(role)
    if message_authors_activity == 30:
        await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 3')
#       role = get(message.author.guild.roles, name="he_is_here")
#       await message.author.add_roles(role)
    if message_authors_activity == 40:
        await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 4')
#       role = get(message.author.guild.roles, name="active")
#       await message.author.add_roles(role)
    if message_authors_activity == 150:
        await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: -1(Bann ha így folytatod!)')
#       role = get(message.author.guild.roles, name="spammer")
#       await message.author.add_roles(role)





    if message_authors_activity < 3:
        role = get(message.author.guild.roles, name="próba")
        await message.author.add_roles(role)
    if 30 > message_authors_activity >= 10:
#               await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 2')
        role = get(message.author.guild.roles, name="not_active")
        await message.author.add_roles(role)
    if 40 > message_authors_activity >= 30:
#               await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 3')
        role = get(message.author.guild.roles, name="he_is_here")
        await message.author.add_roles(role)
    if 150 > message_authors_activity >= 40:
#              await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: 4')
        role = get(message.author.guild.roles, name="active")
        await message.author.add_roles(role)
    if message_authors_activity >= 150:
#             await message.channel.send(f'Nem csak Sáriné ad levelt! Most az Én szememben is nőttél {message.author}! Íme a leveled: -1(Bann ha így folyt$
        role = get(message.author.guild.roles, name="spammer")
        await message.author.add_roles(role)














    if message_authors_activity < 3:
        await message.author.remove_roles(get(message.author.guild.roles, name="not_active"))
        await message.author.remove_roles(get(message.author.guild.roles, name="he_is_here"))
        await message.author.remove_roles(get(message.author.guild.roles, name="active"))
        await message.author.remove_roles(get(message.author.guild.roles, name="spammer"))
    if 30 > message_authors_activity >= 10:
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











    if client.user == message.author:
        return
    if message.author.id != 701859066615431269 and 270904126974590976 and 819241321805643788 and 468281173072805889 and 235088799074484224 and 159985870458322944:
        number_of_pixels = i % 8
        cycle = i / 8

        clear()
        show()
        for x in range(number_of_pixels):
            h = cycle % 10 / 10
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            set_pixel(x, r, g, b)



        i += 1
        show()
        print(message.author)
    with open(data_dict_of_message_authors_file, 'wb') as output_file:
        pickle.dump(data_dict_of_message_authors, output_file)


    if message.channel.id == 825019154045337660:
        #message_channel2 = client.get_channel(825019154045337660)
        response = await rs.get_ai_response(message.content)
        await message.channel.send(response)
        print(response)

    if message.content.startswith('mi_lesz_ekkor'):
        datum = get_just_the_number(message.content)
        message_channel = client.get_channel(821351000144609290)
        try:
            for event in cal.timeline.on(arrow.get(2021, 4, datum)):
                text = f'Esemény: {event.name}: \n{event.description}. Ekkor kezdődik: {event.begin}\n És ekkor fejeződik be: {event.end}'
                await message_channel.send(text)
        except ValueError:
            await message_channel.send('Ilyen nap áprilisban nincs sajna!')

client.run("ODA2OTYzMDY2Nzc5NDY3Nzk2.YBxE6w.rPwvxs08Mx4Lhs-XANQZjv_imb0")

