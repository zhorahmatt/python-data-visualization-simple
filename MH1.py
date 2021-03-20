import tweepy
import json

#Initialize authentification
consumer_key = 'iHujLsC8W4rM0ry91BLeTpj98'
consumer_secret = 'vdcgSw4i3bHg9rfWNNJuix4kIyy7I41eR8JVl9KR60iy6oseRw'
access_token = '390473986-PT6aWvZTeVU9b60G92yqepZX2ok5GRL0D6YYQowp'
access_token_secret = 'oGXzc9lDmlC7Jjlw9ln1HQb88sPic6wbdLVuL9grOtmOJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets():
#fetch tweets from API
    i = 1
    with open('MentalHealth100321.json', 'w') as f:
        for tweet in tweepy.Cursor(api.search, q="Mental Health OR Kesehatan Mental -filter:retweets", result_type="recent", include_entities=True, lang="id",tweet_mode="extended").items():
            a1 = {}
            a1["created_at"] = tweet._json["created_at"]
            a1["geo"] = tweet._json["geo"]
            a1["user"] = tweet._json["user"]["screen_name"]
            a1["full_text"] = tweet._json["full_text"]
            a1["favorite_count"] = tweet._json["favorite_count"]
            a1["retweet_count"] = tweet._json["retweet_count"]
            a1["in_reply_to_screen_name"] = tweet._json["in_reply_to_screen_name"]
            a1["is_quote_status"] = tweet._json["is_quote_status"]


            if tweet._json["retweet_count"] > 0:
                f.write(json.dumps(a1)+"\n")
                print(i, tweet.created_at, tweet.user.screen_name, "Tweeted:", tweet.full_text,".", "Liked: ", tweet.favorite_count, "Retweeted:", tweet.retweeted, 'Count:', tweet.retweet_count)
                i = i + 1


fetch_tweets()
