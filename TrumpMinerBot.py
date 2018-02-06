import tweepy
from tweepy import OAuthHandler

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
        if data.isInstance(Status):
            print(data.text)
        else:
            print("not status")
        return true

    def on_error(self, status):
        print(status)
        return true

myStreamListener = MyListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow="realDonaldTrump")
