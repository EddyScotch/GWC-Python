# Imports
import time
import random
import tweepy


# Keys and Access Tokens

CONSUMER_KEY    = 'mSTtroYHkp0Mr8NwqTADik9cT'
CONSUMER_SECRET = 'E3dcCbn9C4T075DfHXk1Y2sPQ32j9wIJBNOJVxpnWQ0sH8pCH0'

ACCESS_TOKEN    = '1017154520084647937-9xwRBk0EuK7yrqVILWZVZvkpZiKYEL'
ACCESS_SECRET   = 'JtycHM4iHXOXv2guDOiPSyxGjb0eaL7upGhTKZHhwcIty'

tweets = ["I like turtles", "Dogs are awesome", "Hello", "You're a snacc"]
# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)


# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets) - 1)
    api.update_status (tweets [index] + str(count))
    time.sleep (86400)
