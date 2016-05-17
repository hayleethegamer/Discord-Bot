import Settings
import Simple_Commands
import Chat_Commands
import NonCommand_Chat
import Admin_Commands
from Functions import getTime, fileRead, varChange
import importlib

import discord

user = discord.User()
client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + Settings.user)
    print('ID: ' + Settings.id)
    if "workOn = 1" in fileRead("Vars/WorkOn.txt"):
        await client.change_status(discord.Game(name="Being Worked on"))
    if "restart=1" in fileRead("Vars/restart.txt"):
        await client.send_message(fileRead("Vars/restartChannel.txt"),"Done")	
        varChange("restart.txt","restart=0")

@client.event
async def on_message(message):
    print(message.channel.name)
    user = "{0.author.name}"
    try:
        print(getTime() + " " + message.channel.server.name + ": " + message.channel.name + ": " + user.format(message) + ": " + message.content)
    except AttributeError:
        print(getTime() + "PM: " + " " + user.format(message) + ": " + message.content)
    if message.content.startswith('!deleteme'):
        msg = await client.send_message(message.channel, 'I will delete myself now...')
        await client.delete_message(msg)
    if (message.content.startswith("!reload")) and (user.format(message) == "Hayleethegamer"):
        importlib.reload(Simple_Commands)
        importlib.reload(Chat_Commands)
        importlib.reload(NonCommand_Chat)
        importlib.reload(Admin_Commands)
        await client.send_message(message.channel,"Commands Reloaded " + user.format(message))
    await Simple_Commands.simpleCommands(message,client,user)
    await Chat_Commands.chatCommands(message,client,user)
    await NonCommand_Chat.noncommandChat(message,client,user)
    await Admin_Commands.adminCommands(message,client,user)
    if "addsimple=1" in fileRead("Vars/addSimple.txt"):
        importlib.reload(Simple_Commands)
        varChange("addSimple.txt","addsimple=0")
        print("reloaded Simple")

#@client.event
#async def on_message_delete(message):
    #fmt = '{0.author.name} has deleted the message:\n{0.content}'
    #await client.send_message(message.channel, fmt.format(message))

client.run('[token censored]')
