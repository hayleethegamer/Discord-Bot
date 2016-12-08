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
#from Quote_and_Dictionary_Discord import quote, dictionary
import Blame_Command
import Help_Command
from Functions import sendMessage, varChange, fileRead
import json
#import discord
import importlib
import random
from fractions import Fraction
import string
import statistics
import Voting

async def chatCommands(message,client,addBlame,helped,voted,platform,messageObject):
	user = messageObject.user
	message2 = messageObject.message
	me = ["hayleethebot", "hayleebot","<@180867799168712705>","<@180815771172077569>"]
	commandUser = ["myself", "me", "my"]
	old = ["thineself", "thyself"] 
	hayleeGamer = ["haylee","hayleethegamer","hayleegamer","<@167744970952933376>"]
	oddHayleeGamer = ["hayiee","hayle","hayl33"]
	oddCharacters = ["â","„","®","Ž","ℎ","℮","ÿ","ë"]
	puncutation = [",",".","?","!","'",'"',"*",":","`","~","_","@","#",";",":"]
	puncutation = "".join(puncutation)
	echoNoName = ["Hayleethegamer"]
	danceGifs = ["http://haylee.pearachute.net/Images/Discord/kid_scooby_Dance.gif","http://haylee.pearachute.net/Images/Discord/tumblr_mwo4ewEx9T1rxinpyo1_500.gif"]
	if message2.lower().startswith("!quote"):
		#await sendMessage(message,client,platform,"This is currently not working, sorry.")
		#quote(message,user,client)
		with open("Quotes.json") as data_files:
			data = json.load(data_files)
		with open("Quotes_words.json") as data_files:
			dataWord = json.load(data_files)
		try:
			split = message2.lower().split()
			giver = split[1]
			quote = split[2:len(split)]
			try:
				quoteTest = "".join(quote)
				int(quoteTest)
				quote = quoteTest
				quoteNum = True
				#await sendMessage(message,client,platform,"Number Quote")
			except ValueError:
				quote = " ".join(quote)
				quoteNum = False
				#await sendMessage(message,client,platform,"Word Quote ValueError")
			except TypeError:
				quote = " ".join(quote)
				quoteNum = False
				#await sendMessage(message,client,platform,"Word Quote TypeError")
				
			await randomQuote(message,message2,client,user,platform,quote,data,dataWord,giver,quoteNum)
		except IndexError:
			giver = "null"
			quote = "0"
			quoteNum = False
			await randomQuote(message,message2,client,user,platform,quote,data,dataWord,giver,quoteNum)
	#TroubleMaker command
	elif message2.lower().startswith("!troublemaker"):
		try:
			split = message2.split()
			trouble = split[1]
			
			if trouble != "":
				await sendMessage(message,client,platform,"Well well if it isn't the troublemaker " + trouble)
			elif trouble in me:
				await sendMessage(message,client,platform,"So " + user + " you think I'm a trouble maker? Well your a trouble maker for thinking so.")
			elif trouble in commandUser:
				await sendMessage(message,client,platform,"Well well if it isn't the troublemaker " + user.format(message))
			elif trouble in old:
				await sendMessage(message,client,platform,"Wait, are you a trouble maker from the 1560s?")
			else:
				await sendMessage(message,client,platform,"Well well if it isn't the trouble maker...")
		except IndexError:
			trouble = "null"
			await sendMessage(message,client,platform,"Well well if it isn't the trouble maker...")
	#Thanks Command
	elif message2.lower().startswith("!thanks"):
		try:
			split = message2.split()
			thanked = split[1]
			await sendMessage(message,client,platform,"Thank you " + thanked)
		except IndexError:
			thanked = "null"
			await sendMessage(message,client,platform,"Thank you!")
	#Blame Command
	elif message2.lower().startswith("!blame"):
		if addBlame == 1:
			importlib.reload(Blame_Command)
			addBlame = 0
			print("reloaded Blame")
		if await Blame_Command.blameCommand(message,message2,client,user,platform) != True:
			await sendMessage(message,client,platform,"Who is to blame?")
	#Night Command
	elif message2.lower().startswith("!night"):
		try:
			split = message2.split()
			byed = split[1:len(split)]
			byed = " ".join(byed)
			await sendMessage(message,client,platform,"Good night " + byed)
		except IndexError:
			byed = "null"
			await sendMessage(message,client,platform,"Good night")

	#Ban Command
	elif message2.lower().startswith("!ban"):
		try:
			split = message2.split()
			banned = split[1]
			banned = banned.strip(puncutation)
			time = split[2:len(split)]
			time = " ".join(time)
			oddCharNum = 0
			oddCharFound = 0
			printedBan = 0
			#print(banned + " " + time)
			if (banned == "") or (time == ""):
				await sendMessage(message,client,platform,"Who am I banning and for how long?")
			elif ("*" in banned.lower()) or ("~" in banned.lower()):
				await sendMessage(message,client,platform,"Sorry, can't format it mid word, try again")
			elif banned.lower() in me:
				await sendMessage(message,client,platform,"Sorry, I'm not banning myself.")
			elif banned.lower() in commandUser:
				await sendMessage(message,client,platform,"Ok, banning " + user + " for " + time)
			elif banned.lower() in old:
				await sendMessage(message,client,platform,"Wait, are we back in the 1560s?")
			elif banned.lower() in hayleeGamer:
				await sendMessage(message,client,platform,"Sorry, can't ban my creator, and I have half a mind to ban you for trying :stuck_out_tongue:")
			elif banned.lower() in oddHayleeGamer:
				await sendMessage(message,client,platform,"I think you mispelt, could be wrong but yeah... I don't think HAYLEE is spelt " + banned.upper() + " (" + banned.lower() + ")")
			else:
				while oddCharNum <= len(oddCharacters):
					#print(oddCharNum)
					#print (len(oddCharacters))
					oddCharNum = oddCharNum + 1
					try:
						if (oddCharacters[oddCharNum] in banned) and (oddCharFound == 0):
							await sendMessage(message,client,platform,"The heck even is that character?")
							oddCharFound = 1
							printedBan = 1
					except IndexError:	
						if printedBan == 0:
							await sendMessage(message,client,platform,"OK, banning " +banned + " for " + time)
							printedBan = 1
		except IndexError:
			banned = "null"
			time = "null"
			await sendMessage(message,client,platform,"Who am I banning and for how long?")
			#await sendMessage(message,client,platform,"Error")
			#print(split)
	#Buggy Command
	elif message2.lower().startswith("!buggy"):
		try:
			split = message2.split()
			buggy = split[1:len(split)]
			buggy = " ".join(buggy)
			if "hayleethebot" in buggy.lower():
				await sendMessage(message,client,platform,"Wait! I'm not buggy!")
			elif buggy == "":
				await sendMessage(message,client,platform,"What's Buggy?")
			else:
				await sendMessage(message,client,platform,"Yeah, " + buggy + " is very buggy")
		except IndexError:
			buggy = "null"
			await sendMessage(message,client,platform,"What's buggy?")
	#Stalker Command
	elif message2.lower().startswith("!stalker"):
		try:
			split = message2.split()
			stalked = split[1]
			stalker = split[2]
			await sendMessage(message,client,platform,"Why are you stalking " + stalked + " " + stalker)
		except IndexError:
			stalker = "null"
			stalked = "null"
			await sendMessage(message,client,platform,"Who's stalking who? (Stalked then Stalker)")
	#Lazy Command
	elif message2.lower().startswith("!lazy"):
		try:
			split = message2.split()
			lazy = split[1]
			lazy = split[1:len(split)]
			lazy = " ".join(lazy)
			lazy = lazy.lower()
		except IndexError:
			lazy = "Null"
		with open("Lazy.json") as data_files:
			data = json.load(data_files)
		try:
			await sendMessage(message,client,platform,data[lazy])
		except KeyError:
			await sendMessage(message,client,platform,"Sorry, but that was an invalid name, I do not know about this person in relation to laziness")

	#Echo Command
	elif message2.lower().startswith("!echo"):
		if platform == "discord":
			split = message2.split()
			echo = split[1:len(split)]
			echo = " ".join(echo)
			if echo == "":
				await sendMessage(message,client,platform,"What am I echoing?")
			else:
				#if user.format(message) in echoNoName:
				await sendMessage(message,client,platform,echo)
				#else:
					#await sendMessage(message,client,platform,user.format(message) + " echoed: " + echo)
	#Help Command
	elif (message2.lower().startswith("!help")) or (message2.lower().startswith("!halp")):
		if helped == 1:
			importlib.reload(Help_Command)
			helped = 0
			print("reloaded Help")
		await Help_Command.help(message,message2,client,user,platform)
	#Hello chance Command
	elif message2.lower().startswith("!hellochance"):
		hellos = fileRead("Greetings.txt").split()
		hellosNum = len(hellos)
		chanceFaction = "1/" + str(hellosNum)
		percent = (1 * 100)/hellosNum
		await sendMessage(message,client,platform,"The chance is " + chanceFaction + " as a fraction, as a percent "+ str(percent) + "%")
	#tp Command
	elif message2.lower().startswith("!tp"):
		try:
			split = message2.split()
			person = split[1]
			place = split[2:len(split)]
			place = " ".join(place)
			await sendMessage(message,client,platform,"Teleporting " + person + " to " + place)
		except IndexError:
			person = "null"
			place = "null"
			await sendMessage(message,client,platform,"Who is teleporting where?")
	#Shotgun Command
	elif message2.lower().startswith("!shotgun"):
		try:
			oddCharNum = 0
			oddCharFound = 0
			printedShotgun = 0
			split = message2.split()
			person = split[1:len(split)]
			person = " ".join(person)
			person = person.strip(puncutation)
			if person == "":
				await sendMessage(message,client,platform,user + " please don't tell me I gotta use my shotgun.")
			elif person == "pull":
				await sendMessage(message,client,platform,"oooo, I get to play with my shotgun")
			elif ("*" in person.lower()) or ("~" in person.lower()):
				await sendMessage(message,client,platform,"Sorry, can't format it mid word, try again")
			elif person.lower() in me:
				await sendMessage(message,client,platform,"Sorry, I'm not able to shotgun myself.")
			elif person.lower() in commandUser:
				await sendMessage(message,client,platform,"I don't know why but ok, I will shotgun you " + user.format(message))
			elif person.lower() in old:
				await sendMessage(message,client,platform,"Wait, are we back in the 1560s?")
			elif person.lower() in hayleeGamer:
				await sendMessage(message,client,platform,"Sorry, can't shotgun my creator, and I have half a mind to shotgun you for trying :stuck_out_tongue:")
			elif person.lower() in oddHayleeGamer:
				await sendMessage(message,client,platform,"I think you mispelt, could be wrong but yeah... I don't think HAYLEE is spelt " + person.upper() + " (" + person.lower() + ")")
			else:
				while oddCharNum <= len(oddCharacters):
					#print(oddCharNum)
					#print (len(oddCharacters))
					oddCharNum = oddCharNum + 1
					try:
						if (oddCharacters[oddCharNum] in person) and (oddCharFound == 0):
							await sendMessage(message,client,platform,"The heck even is that character?")
							oddCharFound = 1
							printedShotgun = 1
					except IndexError:	
						if printedShotgun == 0:
							await sendMessage(message,client,platform,"Sorry " + person + " but you better back off or you will get a shotgun to the face!")
							printedShotgun = 1
		except IndexError:
			person = "null"
			await sendMessage(message,client,platform,user + " please don't tell me I gotta use my shotgun.")
	#Chance Command
	elif message2.lower().startswith("!chance"):
		try:
			split = message2.split()
			try:
				happened = split[1]
				pool = split[2]
				total = split [3]
			except IndexError:
				happened = split[1]
				total = split[2]
				pool = "null"
			if (happened == "") or (pool == "") or (total == ""):
				await sendMessage(message,client,platform,"What and I figureing? (What happened then total, you can also do a fraction for what happened)")
			elif pool == "null":
				chanceFaction = int(happened)/int(total)
				chanceFaction = Fraction(chanceFaction)
				percent = (int(happened) * 100)/int(total)
				await sendMessage(message,client,platform,"The chance is " + str(chanceFaction) + " as a fraction, as a percent "+ str(percent) + "%")
			else:
				chanceFaction = (int(happened)/int(pool))**int(total)
				chanceFaction = Fraction(chanceFaction)
				percent = ((int(happened)/int(pool)) * 100)/int(total)
				await sendMessage(message,client,platform,"The chance is " + str(chanceFaction) + " as a fraction, as a percent "+ str(percent) + "%")
		except IndexError:
			happened = "null"
			total = "null"
			await sendMessage(message,client,platform,"What and I figureing? (What happened then total, you can also do a fraction for what happened)")
	#English Command
	elif message2.startswith("!english"):
		try:
			split = message2.split()
			language = split[1]
			#"What is English?" Is the standard"
			with open("English.json") as data_files:
				data = json.load(data_files)
			languageList = list(data["Languages"][0].keys())
		
			if(language == ""):
				language = random.choice(languageList)
				language = language[0]
				language = language.lower()
				await sendMessage(message,client,platform,data["Languages"][0][language])
			else:
				await sendMessage(message,client,platform,data["Languages"][0][language])
		except IndexError:
			language = "null"
			#"What is English?" Is the standard"
			with open("English.json") as data_files:
				data = json.load(data_files)
			languageList = list(data["Languages"][0].keys())
			language = random.sample(languageList,1)
			language = language[0]
			language = language.lower()
			await sendMessage(message,client,platform,data["Languages"][0][language])
	#Random Command
	elif message2.startswith("!random"):
		try: 
			split = message2.split()
			toRandom = split[1]
			toRandom = toRandom.lower()
			randomLetters =[]
			times = random.randint(1,20)
			timesDone = 0
			if toRandom == "letters":
				while timesDone <= times:
					timesDone = timesDone + 1
					randomLetters.append(random.choice(string.ascii_letters))
			elif toRandom == "numbers":
				while timesDone <= times:
					timesDone = timesDone + 1
					randomLetters.append(random.choice(string.digits))
			randomLetters = "".join(randomLetters)
			await sendMessage(message,client,platform,randomLetters)
		except IndexError:
			randomLetters =[]
			times = random.randint(1,20)
			timesDone = 0
			while timesDone <= times:
				timesDone = timesDone + 1
				randomLetters.append(random.choice(string.ascii_letters))
			randomLetters = "".join(randomLetters)
			await sendMessage(message,client,platform,randomLetters)
	#Dice Command
	elif message2.startswith("!dice"):
		try:
			split = message2.split()
			sides = int(split[1])
			if sides > 100:
				await sendMessage(message,client,platform,"I am not rolling a dice with more then 100 sides")
				sides = 100
			try:
				times = int(split[2])
				if times > 100:
					await sendMessage(message,client,platform,"I am not rolling the dice more then 100 times")
					times = 100
			except IndexError:
				times = 1
			timesRolled = 1
			result = []
			numResult = []
			if sides == 1:
				await sendMessage(message,client,platform,"Why do you want me to roll a 1 sided dice?")
			else:
				while timesRolled <= times:
					timesRolled = timesRolled + 1
					result.append(str(random.randint(1,sides)))
					numResult.append(random.randint(1,sides))
				result = ", ".join(result)
				#mode = statistics.mode(numResult)
				await sendMessage(message,client,platform,"The Result(s) is/are " + result)#+ ", the mode is " + str(mode))
		except ValueError:
			await sendMessage(message,client,platform,"Whole numbers only please.")
		except IndexError:
			await sendMessage(message,client,platform,"How many sides the dice have? and how many times and I rolling?")
		except TypeError:
			await sendMessage(message,client,platform,"Last I checked, you need a number to tell how many sides there are")
	#Dance Command
	elif message2.lower().startswith("!dance"):
		await sendMessage(message,client,platform,random.choice(danceGifs))
	#flashback Command
	elif message2.lower().startswith("!flashback"):
		try:
			split = message2.lower().split()
			person = split[1]
			flashback = split[2]
			with open("Flashback.json") as data_files:
				data = json.load(data_files)
			try:
				await sendMessage(message,client,platform,data[person][0][flashback])
			except KeyError:
				await sendMessage(message,client,platform,"Sorry but this person/flashback is not in my records")
		except IndexError:
			await sendMessage(message,client,platform,"Who's flashback and which one?")
	#Voting Command
	elif (message2.lower().startswith("!vote")) and (platform == "discord"):
		if voted == 1:
			importlib.reload(Voting)
			voted = 0
			print("reloaded Vote")
		await Voting.voting(message,client,platform,messageObject)
	#TQ Shotgun
	elif message2.lower().startswith("!tqshotgun"):
		if user.lower() == "turtlequeen45":
			await sendMessage(message,client,platform,"Here you go TQ, here's your shotgun")
		else:
			await sendMessage(message,client,platform,"Sorry, but this is TQ's shotgun")
	#Role display
	elif message2.lower().startswith("!displayroles") and (platform == "discord"):
		count = 1
		roles = []
		while count < len(message.author.roles):
			roles.append(message.author.roles[count].name)
			count = count + 1
		roles = "\n".join(roles)
		await sendMessage(message,client,platform,"Your roles are: \n" + roles)
		
	
		
		
		
		
async def randomQuote(message,message2,client,user,platform,quote,data,dataWord,giver,quoteNum):
	if " list" in message2.lower():
		giversList = list(data.keys())
		givers = ", ".join(giversList)
		if quote == "":
			await sendMessage(message,client,platform,"There are " + str(len(giversList)) + " givers, " + givers + " and there are varying number of quotes to each(!quote list [giver]")
		elif quote == "all":
			count = 0
			totalQuotes = 0
			while count <= len(giversList)-1:
				quote = giversList[count]
				totalQuotes = totalQuotes + len(data[quote])
				count = count + 1
			await sendMessage(message,client,platform,"There are " + str(totalQuotes) + " quotes recorded.")
		else:
			await sendMessage(message,client,platform,quote.title() + " has " + str(len(data[quote])) + " quotes.")
		
	elif (giver == "random") or (quote == "r a n d o m") or (quote == "random"):
		giversList = list(data.keys())
		if giver == "random":
			giver = random.choice(giversList)
			giver = giver.lower()
		try:
			quoteList = data[giver]
			quote = random.choice(quoteList)
			qList = data[giver].index(quote)
			quote = str(qList+1)
		except KeyError:
			await sendMessage(message,client,platform,"Sorry, Invalid Giver/quote")
			return
		#await sendMessage(message,client,platform,"Giver: " + giver)
		#await sendMessage(message,client,platform,"Quote: " + str(quote))
		#await sendMessage(message,client,platform,"List: " + str(list))
		#await sendMessage(message,client,platform,"Hello! :D")
		try:
			await sendMessage(message,client,platform,data[giver][qList][quote])
		except KeyError:
			await sendMessage(message,client,platform,"Sorry, Invalid Giver/quote")
	elif(giver == "") or (quote == ""):
		await sendMessage(message,client,platform,"Who gave the quote and which quote?")
	else:
		try:
			if quoteNum == True:
				qList = int(quote) - 1
				await sendMessage(message,client,platform,data[giver][qList][quote])
			else:
				await sendMessage(message,client,platform,dataWord[giver][0][quote])
		except KeyError:
			#await sendMessage(message,client,platform,"Giver: " + giver)
			#await sendMessage(message,client,platform,"Quote: " + quote)
			#await sendMessage(message,client,platform,"List: " + str(list))
			await sendMessage(message,client,platform,"Sorry, Invalid Giver/quote")
	
