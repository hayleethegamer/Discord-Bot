import datetime
async def sendMessage(message,client,sentMessage):
        msg = await client.send_message(message.channel, sentMessage)

def getTime():
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	second = str(now.second)
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	time = (month + " " + day + " " + year + ", " + hour + ":" + minute + ":" + second)
	return time

def varChange(file, write):
	result = open('Files/Vars/' + file,"w").write(write)
	return result

def fileRead(file):
	result = open("Files/" + file).read()
	return result

def codeWrite(file, write):
	result = open(file,"a").write(write + "\n")
	return result

