__author__ = 'achyutjoshi'

import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = '01T07PbzXeV64y7DBTi4S7fJN'
consumer_secret = 'xIrAFBYSgqoheRoL6LBxvYIMeOsOq3JGnIRbJr3MwDddKhaqqo'
access_token = '1951559215-xJyR18EeGXkAg0CyMZTgE5XOYlo14S9oXphGdW3'
access_token_secret = 'q33OYSM148H2nx2PCNjzlloYBODPVCW7lx83s4O2Z72iI'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status(status = 'Hello Python Central!')