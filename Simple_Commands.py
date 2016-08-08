from Functions import sendMessage, varChange, fileRead
#import discord

async def simpleCommands(message,message2,client,user,platform):
	if message2.lower().startswith("!hayleethebot"):
		await sendMessage(message,client,platform,user.format(message) + " I am a bot made by Hayleethegamer. You may also find me on twitch whenever Haylee is streaming. Haylee made me for fun, with much headache for the Discord version, but now I am working, so yeah. How is your day?")
	elif message2.lower().startswith("!bed"):
		await sendMessage(message,client,platform,"Bed? What is a bed? Sleep? what is sleep?")
	elif message2.lower().startswith("!get well"):
		await sendMessage(message,client,platform,"Aw, Get well soon")
	elif message2.lower().startswith("!abuser"):
		await sendMessage(message,client,platform,"Aw, why do you want to abuse me?")
	elif message2.lower().startswith("!rude"):
		await sendMessage(message,client,platform,"Why you gotta be so rude? Don't you know I'm human too")
	elif (message2.lower().startswith("!hayleediscord")) and (user.format(message) == "Hayleethegamer"):
		await sendMessage(message,client,platform,"Wanna come join me and Hayleethegamer away from here? join our discord! [link]")
	elif (message2.lower().startswith("!privatehayleediscord")) and (user.format(message) == "Hayleethegamer"):
		await sendMessage(message,client,platform,"Buggy PMs? Come to Haylee's Private discord for Private messages! :smile: [link])
	elif message2.lower().startswith("!lawyer"):
		await sendMessage(message,client,platform,"You don't have the right to an attorney , if you can not afford to not have one, one will not be appointed to you. You have the right to not remian silent, anything you say can and will be used in a court of law")
	elif message2.lower().startswith("!cut"):
		await sendMessage(message,client,platform,"Oh you wanna cut me " + user.format(message) + "? I'll just shoot you with a shotgun.")
	elif message2.lower().startswith("!questionit"):
		await sendMessage(message,client,platform,"I question everything")
	elif message2.lower().startswith("!request"):
		await sendMessage(message,client,platform,"I do not have a request feature of any kind ATM, Why are you trying?")


	#Commands added with !add command

	elif message2.lower().startswith("!realhaylee"):
		await sendMessage(message,client,platform,"I am the real Haylee! Wait, no, sorry, I'm a bot...")

	elif message2.lower().startswith("!hayleebelief"):
		await sendMessage(message,client,platform,"Everyone should be allowed to do what ever they want as long as it doesn't infringe upon others")

	elif message2.lower().startswith("!party"):
		await sendMessage(message,client,platform,"WOOO! Party!!!!")

	elif message2.lower().startswith("!gg"):
		await sendMessage(message,client,platform,"Welp, Good Game")

	elif message2.lower().startswith("!break"):
		await sendMessage(message,client,platform,"You can't break me that easy")

	elif message2.lower().startswith("!hold"):
		await sendMessage(message,client,platform,"HOLD ON, WAIT, STOP")

	elif message2.lower().startswith("!order66"):
		await sendMessage(message,client,platform,"Yes my Haylee, it shall be done.")

	elif message2.lower().startswith("!stop"):
		await sendMessage(message,client,platform,"I will not stop! I stop for no one! (Except Haylee...)")

	elif message2.lower().startswith("!birthday"):
		await sendMessage(message,client,platform,"HAPPY BIRTHDAY!!!! http://haylee.pearachute.net/Images/Discord/birthday_fireworks.gif")

	elif message2.lower().startswith("!rip"):
		await sendMessage(message,client,platform,"Welp Rest in peace")
	elif message2.lower().startswith("!pun"):
		await sendMessage(message,client,platform,"There's no punishment for bad puns, only punitive damages")

	elif message2.lower().startswith("!bark"):
		await sendMessage(message,client,platform,"bark bark get the thing")

	elif message2.lower().startswith("!can'texplain"):
		await sendMessage(message,client,platform,"'I'm afraid I can't explain my self... I'm not the girl I used to be' (Just a Dream (feat. Tasha Baxter) by Tut Tut child)")

	elif message2.lower().startswith("!4k"):
		await sendMessage(message,client,platform,"http://haylee.pearachute.net/Images/Discord/4k-image-tiger-jumping.jpg")
