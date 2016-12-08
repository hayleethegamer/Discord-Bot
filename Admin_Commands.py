'''Copyright (C) 2016 Hayleethegamer 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
import sys
import subprocess
from Functions import sendMessage, varChange, fileRead, codeWrite
import discord

async def adminCommands(message,client,user):
	if (user.format(message) == "Hayleethegamer"):
		#To restart the bot, Broken
		if message.content.startswith("!restart"):
			await sendMessage(message,client,"Restarting...")
			varChange("restart.txt","restart=1")
			channel = str(message.channel.name)
			varChange("restartChannel.txt",channel)
			subprocess.call("Files/RestartBot.sh")
			sys.exit()
		elif message.content.startswith("!WIP"):
			if "start" in message.content:
				await sendMessage(message,client,"Nice, I'm getting an upgrade! :D")
				await client.change_status(discord.Game(name="Being Worked on"))
				varChange("WorkOn.txt", "workOn = 1")
			elif "done" in message.content:
				await sendMessage(message,client,"Thanks " + user.format(message) + " for upgrading me! :smile:")
				await client.change_status(None)
				varChange("WorkOn.txt", "workOn = 0")
		elif message.content.startswith("!change"):
			if "game" in message.content:
				try:
					split = message.content.split()
					game = split[2:len(split)]
					game = " ".join(game)
					if game.lower() == "none":
						await sendMessage(message,client,"OK, my game is nothing now")
						await client.change_status(None)
					else:
						await sendMessage(message,client,"My game is now " + game)
						await client.change_status(discord.Game(name=game))
				except IndexError:
					game = "null"
					await sendMessage(message,client, "What game should I change to?")
		elif message.content.startswith("!add"):
			try:
				split = message.content.split()
				command = split[1]
				result = split[2:len(split)]
				result = " ".join(result)
				if (command == "") or (result == ""):
					await sendMessage(message,client,"What am I adding? (One word command, result of command)")
				else:
					write1 = '\n	elif message.content.startswith("!'
					write2 = '"):\n		await sendMessage(message,client,"'
					write3 = '")'
					write = write1 + command + write2 + result + write3
					codeWrite("Simple_Commands.py",write)
					varChange("addSimple.txt","addSimple=1")
					await sendMessage(message,client,"Command " + command + " added " + user.format(message))
			except IndexError:
				await sendMessage(message,client,"What am I adding? (One word command, result of command)")
