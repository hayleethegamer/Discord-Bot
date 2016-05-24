import Settings
import Simple_Commands
import Chat_Commands
import NonCommand_Chat
import Admin_Commands
from Functions import getTime, fileRead, varChange, logTraceback
import importlib
import sys

import discord

user = discord.User()
client = discord.Client()
osError = False
errors = 0
stopped = 0
#addBlame = 0

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + Settings.user)
    print('ID: ' + Settings.id)
    if "workOn = 1" in fileRead("Vars/WorkOn.txt"):
        await client.change_status(discord.Game(name="Being Worked on"))
    if "restart=1" in fileRead("Vars/restart.txt"):
        #await client.send_message(fileRead("Vars/restartChannel.txt"),"Done")	
        varChange("restart.txt","restart=0")

@client.event
async def on_message(message):
    try:
        #print(message.channel.name)
        user = "{0.author.name}"
        try:
            print(getTime() + " " + message.channel.server.name + ": " + message.channel.name + ": " + user.format(message) + ": " + message.content)
        except AttributeError:
            print(getTime() + " PM: " + " " + user.format(message) + ": " + message.content)
        if message.content.startswith('!deleteme'):
            msg = await client.send_message(message.channel, 'I will delete myself now...')
            await client.delete_message(msg)
        if (message.content.startswith("!reload")) and (user.format(message) == "Hayleethegamer"):
            if "full" in message.content:
                try:
                    importlib.reload(Simple_Commands)
                    importlib.reload(Chat_Commands)
                    importlib.reload(NonCommand_Chat)
                    importlib.reload(Admin_Commands)
                    await client.send_message(message.channel,"Commands Reloaded " + user.format(message))
                    errors = 0
                    stopped = 0
                except:
                    await client.send_message(message.channel,"```" + str(sys.exc_info()[1:2]) + "```")
            else:
                try:
                    importlib.reload(Simple_Commands)
                    importlib.reload(Chat_Commands)
                    importlib.reload(NonCommand_Chat)
                    importlib.reload(Admin_Commands)
                    await client.send_message(message.channel,"Commands Reloaded " + user.format(message))
                    errors = 0
                    stopped = 0
                except:
                    await client.send_message(message.channel,"```" + str(sys.exc_info()[1]) + "```")
        await Simple_Commands.simpleCommands(message,client,user)
        await Chat_Commands.chatCommands(message,client,user)
        await NonCommand_Chat.noncommandChat(message,client,user)
        await Admin_Commands.adminCommands(message,client,user)
        if (message.content.startswith("!add")) and (user.format(message) == "Hayleethegamer"):
            if "addSimple=1" in fileRead("Vars/addSimple.txt"):
                importlib.reload(Simple_Commands)
                importlib.reload(Chat_Commands.Blame_Command)
                varChange("addSimple.txt","addsimple=0")
                #addBlame = 1
            print("reloaded Simple")
        if (message.content.startswith("!error restart")) and (user.format(message) == "Hayleethegamer"):
            errors = 0
            stopped = 0
    except OSError:
        if osError == False:
            osError = True
            await client.send_message(message.channel,"There was an OSError, I am turning  myself now")
            subprocess.call("Files/Kill-9.sh")
            sys.exit(2)
    except: #Exception as ex:
        #error = str(sys.exc_info())
        #codeWrite("Log/Log1.txt",error[1:len(error)])	
        #await client.send_message(message.channel,"```" + error[1:len(error)]) + "``` \n Uh Oh, you found a bug...")
        #logTraceback(ex)
        errors += 1
        if (errors >= 5) and (stopped == 0):
                await sendMessage(message.channel,"Uh oh, I've sent to many errors, I'll stop now")
                stopped = 1
        elif errors <= 5:
                await client.send_message(message.channel,"``` " + str(sys.exc_info()[1:2]) + " ``` \n There was a bug")
            


#@client.event
#async def on_message_delete(message):
    #fmt = '{0.author.name} has deleted the message:\n{0.content}'
    #await client.send_message(message.channel, fmt.format(message))

client.run('MTgwODY3Nzk5MTY4NzEyNzA1.Chgdww.a8FJJkjskukuooYjCsMNlMud6jM')
