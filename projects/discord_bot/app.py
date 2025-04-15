import discord
import os
import requests
import json
import random
import string
from dotenv import load_dotenv


intents = discord.Intents.default()


client = discord.Client(intents=intents)

# special words
sadWords = ["sad","depressed","unhappy","angry","miserable","depressing"]
starterEncouragement = ["Cheer up !","Hang in there","You are a great person / bot"]

# normal words
normalWords = f"{string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.hexdigits + string.octdigits}"
print(normalWords)
def getQuote():
    apiResponse = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(apiResponse.text)
    quote = jsonData[0]['q'] + " -" + jsonData[0]['a']
    return quote



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    clientMsg = message.content 

    strComp =  (word in clientMsg for word in normalWords)
    if clientMsg.startswith("$hello") or strComp:
        botQuote = getQuote()
        await message.channel.send(botQuote)
    
    if any(word in clientMsg for word in sadWords):
        await message.channel.send(random.choice(starterEncouragement))
    
    if not strComp:
        await message.channel.send("?")
    
    
    

load_dotenv()
client.run(os.getenv("TOKEN"))

