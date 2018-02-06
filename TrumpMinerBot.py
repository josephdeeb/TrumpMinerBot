import tweepy
import discord
import asyncio
from tweepy import OAuthHandler

#Add discord client

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('--------')

async def receivedTrumpMessage(content):
    if !content.isinstance(String):
        print("ERROR! Content is not a string")
        return
    for server in client.servers:
        await client.send_message(server, content, tts=True)

client.run('token')

consumer_key = "sv9mBxkyS9IhjeUShxmGnNri5"
consumer_secret = "zrlffyH2s7ywn2IVxHoR6qOwdEsCsvqYGRpAl1AOsFDdcvMwGt"
#Not sure if the dash in access_token is supposed to be there...
access_token = "960957212259577856-QHdTow3q0BbJKyzYloa7bi0BWfeoCZA"
access_secret = "okv9lwKvdZYSyuN8SC9MkWSsaPczhhQVE2NQQMjLcSP1U"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#for status in tweepy.Cursor(api.user_timeline("realDonaldTrump")):
#    print(status.text)

class MyListener(StreamListener):

    def on_data(self, data):
        if data.isinstance(Status):
            receivedTrumpMessage(data.text)
        else:
            print("not status")
        return true

    def on_error(self, status):
        print(status)
        return true

myStreamListener = MyListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow="realDonaldTrump")
