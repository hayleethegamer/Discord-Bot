from Functions import sendMessage
import json
async def help(message,message2,client,user,platform):
		try:
			split = message2.split()
			command = split[1:len(split)]
			command = " ".join(command)
			command = command.lower()
			blamePeople = ["hayleethebot", "echo", "blue","kjay","ISP","sandy","bananas","hayleethegamer"]
			blamePeople = ", ".join(blamePeople)
			simpleCommands = ["hayleethebot", "bed", "get well", "abuser", "rude", "hayleediscord", "lawyer", "cut", "realhaylee", "hayleebelief", "party", "gg", "break", "hold", "dance", "questionit", "order66","stop","birthday","rip","pun","bark","can'texplain","4k"]
			simpleCommands2 = "`, `".join(simpleCommands)
			complexCommands = ["quote", "troublemaker", "thanks", "blame", "night", "ban", "buggy", "stalker", "lazy","hellochance","Shotgun", "english", "random", "dice", "flashback", "voting (broken)","displayroles"]
			complexCommands = "`, `".join(complexCommands)
			with open("Quotes.json") as data_files:
				data = json.load(data_files)
			giversList = list(data.keys())
			with open("English.json") as data_files:
				data = json.load(data_files)
			languageList = list(data["Languages"][0].keys())
			with open("Lazy.json") as data_files:
				data = json.load(data_files)
			lazyList = list(data.keys())
			givers = ", ".join(giversList)
			language = ", ".join(languageList)
			lazy = ", ".join(lazyList)
			with open("Complex_Help.json") as data_files:
				data = json.load(data_files)
			if command == "":
				await sendMessage(message,client,platform,"The current Commands are `" + simpleCommands2 + "`, `" + complexCommands + "`. Some commands need extra to run properly, type '!help [command]' for more information on how to use that command")
			elif command in simpleCommands:
				await sendMessage(message,client,platform,command.capitalize() + " is a 'simple command' so there is nothing to it, just type it in and go")
			elif command == "quote":
				await sendMessage(message,client,platform,"Quote takes a 'giver' and a number, the current givers are " + givers + ". The numbers vary by who the giver is. You can also have it randomly pick quotes with '!quote random' and '!quote [giver] random' You can also do '!quote list' to list the givers and how many quotes they have ('!quote list [giver]')")
			elif command == "blame":
				await sendMessage(message,client,platform,"Blame requires a specific name to work right. these names are " + blamePeople + ". Example: '!blame hayleethebot'")
			elif command == "lazy":
				await sendMessage(message,client,platform,"Lazy requires a name which I know. These names are " + lazy + ". Example: '!lazy haylee'")
			else:
				try:
					await sendMessage(message,client,platform,data[command])
				except KeyError:
					await sendMessage(message,client,platform,"Sorry, that is not a command I have.")

		except IndexError:
			await sendMessage(message,client,platform,"The current Commands are `" + simpleCommands2 + "`, `" + complexCommands + "`. Some commands need extra to run properly, type '!help [command]' for more information on how to use that command")