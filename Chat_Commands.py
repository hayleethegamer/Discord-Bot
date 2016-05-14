def chatCommands(message,client):
	if message.content.startswith("Hello"):
		msg = await client.send_message(message.channel, 'I will delete myself now...')
		sendMessage(message,client,"Hello")
	

def sendMessage(message,client,sentMessage):
	msg = await client.send_message(message.channel, sentMessage)
	
