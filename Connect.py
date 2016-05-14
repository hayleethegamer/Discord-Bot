import Settings
from Chat_Commands import chatCommand

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + Settings.user)
    print('ID: ' + Settings.id)

@client.event
async def on_message(message):
    if message.content.startswith('!deleteme'):
        msg = await client.send_message(message.channel, 'I will delete myself now...')
        await client.delete_message(msg)
    if message.content.startswith("Hello"):
        msg = await client.send_message(message.channel, "Hi")
    chatCommands(message,client)

@client.event
async def on_message_delete(message):
    fmt = '{0.author.name} has deleted the message:\n{0.content}'
    await client.send_message(message.channel, fmt.format(message))

client.run('MTgwODY3Nzk5MTY4NzEyNzA1.Chgdww.a8FJJkjskukuooYjCsMNlMud6jM')
