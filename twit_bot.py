import tweepy
import twitter_account

class account:
    def __init__(self):
        consumer_key= twitter_account['consumer_key']
        consumer_secret= twitter_account['consumer_secret']
        access_key = twitter_account['access_key']
        access_secret = twitter_account['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

    def tweet_min_extreme(self, temp, temp_record):
        self.api.update_status("Toronto's current temperature of {0} C is below the historic record low of {1} C for this date! #extremeweather #torontoweather".format(temp,temp_record))

    def tweet_max_extreme(self, temp, temp_record):
        self.api.update_status("Toronto's current temperature of {0} C is above the historic record high of {1} C for this date! #extremeweather #torontoweather".format(temp,temp_record))

    def tweet_min_avg(self, temp, temp_record):
        self.api.update_status("Toronto's current temperature of {0} C is below the historic average low of {1} C for this date! #extremeweather #torontoweather".format(temp,temp_record))

    def tweet_max_avg(self, temp, temp_record):
        self.api.update_status("Toronto's current temperature of {0} C is above the historic average high of {1} C for this date! #extremeweather #torontoweather".format(temp,temp_record))

    def test_tweet(self,message):
        self.api.update_status(message)

    def custom_message(self,message):
        self.api.update_status(message)