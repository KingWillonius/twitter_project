# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'z9X8gH6FVGxwPnAniVXlaLhXh'
consumer_secret = 'EnZd0nkA0Ayd0q7yO1gKvCIZmccgjEFIe5nkIucTKH6O9WWuDq'
access_token = '986583084677128192-Br1NTPxLGb7elNZRZw9dz1dwqbvnAVa'
access_secret = 'KUqymfvZtrAHZOJBRkTBMFYwRu93CUDYA8w1QwXTxacc0'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
