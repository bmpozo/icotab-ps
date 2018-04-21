import tweepy

def get_auth():
    consumer_key = 'XXX'
    consumer_secret = 'XXX'
    access_token = 'XXX-XXX'
    access_token_secret = 'XXX'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # When a tweet is published it arrives here.
        print(status.text.encode("ascii", errors='replace'))  # Console output may not be UTF-8
        print("-"*10)


if __name__ == '__main__':
    print("===== My Application =====")

    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.

    # Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    print(">> Listening to tweets about #python:")
    myStream.filter(track=['python'])

    # End
    print("c'est fini!")
