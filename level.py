import discord
import json
import os.path

client = discord.Client()

bot = "bot.py"
dir_path = os.path.dirname(os.path.realpath(__file__))
bot_path = dir_path + "/" + bot
restart_on_error = True
wait_before_restart = 3


@client.event
async def on_ready():
    print(client.user.name)
    print("===================")


@client.event
async def on_message(message):
    user_id = message.author.id

    author_level = get_level(user_id)
    author_xp = get_xp(user_id)

    if author_level == 0 and author_xp >= 10:
        set_level(user_id, 1)
        await client.send_message(message.channel, "1 Level Oldun")

    if author_level == 1 and author_xp >= 27:
        set_level(user_id, 2)
        await client.send_message(message.channel, "2 Level oldun")
    if author_level == 2 and author_xp >= 49:
        set_level(user_id, 3)
        await client.send_message(message.channel, "3 Level Oldun")
    if author_level == 3 and author_xp >= 81:
        set_level(user_id, 4)
        await client.send_message(message.channel, "4 Level Oldun")

    if author_level == 4 and author_xp >= 100:
        set_level(user_id, 5)
        await client.send_message(message.channel, "5 Level Oldun")
    
    if author_level == 5 and author_xp >= 250:
        set_level(user_id, 6)
        await client.send_message(message.channel, "6 Level Oldun")

    if author_level == 6 and author_xp >= 378:
        set_level(user_id, 7)
        await client.send_message(message.channel, "7 Level Oldun")

    if author_level == 7 and author_xp >= 518:
        set_level(user_id, 8)
        await client.send_message(message.channel, "8 Level Oldun")

    if author_level == 8 and author_xp >= 798:
        set_level(user_id, 9)
        await client.send_message(message.channel, "9 Level Oldun")

    if author_level == 9 and author_xp >= 1111:
        set_level(user_id, 10)
        await client.send_message(message.channel, "10 Level Oldun")

        lvl_role = None
        for role in message.server.roles:
            if role.name == "level 10":
                lvl_role = role

        await client.add_roles(message.author, lvl_role)

    if message.content.lower().startswith('sa'):
        await client.send_message(message.channel, "as")

    if message.content.lower().startswith('e!xp'):
        await client.send_message(message.channel, "Tam tamına `{}` XP!".format(get_xp(message.author.id)))

    if message.content.lower().startswith('e!lvl'):
        level = get_level(user_id)
        await client.send_message(message.channel, "Mevcut Leveliniz: {}".format(level))

    if author_level == 0:
        user_add_xp(message.author.id, 5)

    if author_level == 1:
        user_add_xp(message.author.id, 4)

    if author_level == 2:
        user_add_xp(message.author.id, 4)

    if author_level == 3:
        user_add_xp(message.author.id, 4)
         
    if author_level == 4:
        user_add_xp(message.author.id, 4)

    if author_level == 5:
        user_add_xp(message.author.id, 3)

    if author_level == 6:
        user_add_xp(message.author.id, 3)

    if author_level == 7:
        user_add_xp(message.author.id, 2)
   
    if author_level == 8:
        user_add_xp(message.author.id, 2)

    if author_level == 9:
        user_add_xp(message.author.id, 2)

    if author_level == 10:
        user_add_xp(message.author.id, 1)


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0



