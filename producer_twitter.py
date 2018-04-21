from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import json

access_token = "XXX-XXX"
access_token_secret =  "XXX"
consumer_key =  "XXX"
consumer_secret =  "XXX"

class StdOutListener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        if 'text' in all_data:
              tweet = all_data["text"]
              created_at = all_data["created_at"]
              retweeted = all_data["retweeted"]
              username = all_data["user"]["screen_name"]
              user_tz = all_data["user"]["time_zone"]
              user_location = all_data["user"]["location"]
              user_coordinates = all_data["coordinates"]
              print (tweet)
              producer.send_messages("test1", tweet.encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['trump'],languages=['en'])
