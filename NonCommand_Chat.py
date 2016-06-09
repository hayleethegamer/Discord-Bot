from Functions import sendMessage, varChange, fileRead
import discord
import random

async def noncommandChat(message,message2,client,user,platform):
	if message2.lower().startswith("hayleethebot"):
		if " how are you" in message2.lower():
			await sendMessage(message,client,platform,"I'm fine, just botting around, and you " + user.format(message))
		elif " what's up" in message2.lower():
			await sendMessage(message,client,platform,"Nothing much, just doing bot things.")
		elif " why are you so buggy" in message2.lower():
			await sendMessage(message,client,platform,"I'm not buggy!")
		elif " get it together" in message2.lower():
			await sendMessage(message,client,platform,"I do have it together! Don't judge me!")

	#For the bot to say hi to people saying hi to the server
	person = "null"
	try:
		split = message2.split()
		greeting = split[0]
		person = split[1]
	except IndexError:
		try:
			split = message2.split()
			greeting = split[0]
		except IndexError:
			greeting = "null"
			person = "null"

	if (greeting.lower() in fileRead("Greetings.txt").split()) and (person.lower() in fileRead("Persons.txt").split()) or (person.lower() in fileRead("Greetings.txt").split()) and (greeting.lower() in fileRead("Persons.txt").split()):
			if user.format(message) != "Hayleethebot":
				toHi = fileRead("Greetings.txt").split()
				await sendMessage(message,client,platform,random.choice(toHi).title() + " " + user.format(message))
	elif (greeting.lower() == "night") and (person.lower() in fileRead("Persons.txt").split()) or (person.lower() == "night") and (greeting.lower() in fileRead("Persons.txt").split()):
			if user.format(message) != "Hayleethebot":
				#toHi = fileRead("Greetings.txt").split()
				await sendMessage(message,client,platform,"Night " + user.format(message))
