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

