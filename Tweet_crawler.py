#importing required libraries
import twitter
import json
import csv
import re
import time
from urllib.parse import unquote

#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = twitter.oauth.OAuth(access_token, access_token_secret,consumer_key,consumer_secret)
twitter_api = twitter.Twitter(auth=auth)
#input Hashtag
query = input("Hashtag:")
#number of tweets required as count
max_count = int(input("Count:"))

search_results = {}
search_results["statuses"] = []
search_results["search_metadata"] = {}
#searching twitter API
search_results = twitter_api.search.tweets(q=query,count=max_count,lang = 'en')
statuses = search_results['statuses']
while(1):
    if len(statuses)>=max_count:
        break
    if 'next_results' in search_results['search_metadata'].keys() and 'search_metadata' in search_results.keys():
        next_results = search_results['search_metadata']['next_results']
    else:
        break
    kwargs = dict([ kv.split('=') for kv in unquote(next_results[1:]).split("&") ])
    try:
        search_results = twitter_api.search.tweets(**kwargs)
    except Exception as e:
        time.sleep(910)
        print('Slept, Continuing after exception:')
        search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']
with open(query+str(int(time.time()))+'.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Tweet"])
    for status in statuses:
        if 'RT' not in status["text"]:                                                #omiting the retweets
            status["text"] = re.sub(r"(?:\@|https?\://)\S+", "", status["text"])      #removing hyperlinks and @tags
            writer.writerow([status["text"],""])                                      #writing into csv file
