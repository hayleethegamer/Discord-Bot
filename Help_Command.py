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
from Functions import sendMessage
import json
async def help(message,message2,client,user,platform):
		try:
			split = message2.split()
			command = split[1:len(split)]
			command = " ".join(command)
			command = command.lower()
		except IndexError:
			command = None
		blamePeople = ["hayleethebot", "echo", "blue","kjay","ISP","sandy","bananas","hayleethegamer"]
		blamePeople = ", ".join(blamePeople)
		simpleCommands = ["hayleethebot", "bed", "get well", "abuser", "rude", "hayleediscord", "lawyer", "cut", "realhaylee", "hayleebelief", "party", "gg", "break", "hold", "dance", "questionit", "order66","stop","birthday","rip","pun","bark","can'texplain","4k"]
		simpleCommands2 = "`, `".join(simpleCommands)
		complexCommands = ["quote", "troublemaker", "thanks", "blame", "night", "ban", "buggy", "stalker", "lazy","hellochance","Shotgun", "english", "random", "dice", "flashback", "voting (broken)","displayroles"]
		complexCommands = "`, `".join(complexCommands)
		if command == "" or command == None:
			await sendMessage(message,client,platform,"hi")
			await sendMessage(message,client,platform,"The current Commands are `" + simpleCommands2 + "`, `" + complexCommands + "`. Some commands need extra to run properly, type '!help [command]' for more information on how to use that command")
		elif command in simpleCommands:
			await sendMessage(message,client,platform,command.capitalize() + " is a 'simple command' so there is nothing to it, just type it in and go")
		elif command == "quote":
			with open("Quotes.json") as data_files:
				data = json.load(data_files)
			giversList = list(data.keys())
			givers = ", ".join(giversList)
			await sendMessage(message,client,platform,"Quote takes a 'giver' and a number, the current givers are " + givers + ". The numbers vary by who the giver is. You can also have it randomly pick quotes with '!quote random' and '!quote [giver] random' You can also do '!quote list' to list the givers and how many quotes they have ('!quote list [giver]')")
		elif command == "blame":
			await sendMessage(message,client,platform,"Blame requires a specific name to work right. these names are " + blamePeople + ". Example: '!blame hayleethebot'")
		elif command == "lazy":
			with open("Lazy.json") as data_files:
				data = json.load(data_files)
			lazyList = list(data.keys())
			lazy = ", ".join(lazyList)
			await sendMessage(message,client,platform,"Lazy requires a name which I know. These names are " + lazy + ". Example: '!lazy haylee'")
		elif command == "english":
			with open("English.json") as data_files:
				data = json.load(data_files)
			languageList = list(data["Languages"][0].keys())
			language = ", ".join(languageList)
			await sendMessage(message,client,platform,"English can be used just as !english or you can tell it to use a specific language, the languages currently in the command are " + language)
		else:
			try:
				with open("Complex_Help.json") as data_files:
					data = json.load(data_files)
				await sendMessage(message,client,platform,data[command])
			except KeyError:
				await sendMessage(message,client,platform,"Sorry, that is not a command I have.")
