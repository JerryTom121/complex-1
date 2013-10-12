'''
Created on Oct 6, 2013

@author: ivan
'''
import oauth2 as oauth
import json

consumer_key = "1421319247-XTrjGKTyEZu4h5duCpvT4VnWycdySzmzzgNMutP"
consumer_secret = "gGZQ7ZJlTpZLyx6q14bssIx9qKhU9Z4e9pVERVMV8"


oauth_token = "NON0gkzkjARUT5nSbHah7A"
oauth_token_secret ="UOM1s70nRjOdf91dCvGKospyM0KMiJRLudATTQBmqMs" ;

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth.Token(key=oauth_token, secret=oauth_token_secret)
client = oauth.Client(consumer, access_token)

terms = json.dumps({'track' : 'twitter'})
stream_endpoint = "https://stream.twitter.com/1.1/statuses/filter.json"
response, data = client.request(stream_endpoint,"POST")

print response, data;
