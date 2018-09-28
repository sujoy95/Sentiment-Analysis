#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#import the library
import tweepy
from textblob import TextBlob

#establishing the user authorization with twitter
consumer_key ="OAnJt97orZf946wJ6dP7Q46M2"
consumer_secret="d4kQ0esPZrjGjOTntw70cayp13YhGzKWuo3RivA3rJaFd5Etvd"
access_token="490491116-OHjLgMpPnfTEfii44cOKuDMZD3kodHxPtYkTNuTI"
access_token_secret="Jt9IJMXzEU6uvJkcfoRGrQ1RtEplE2myT6uf1H1e2EsaJ"

#connecting with twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#fetch the keyword and no. of tweets
searchword = input("Enter the Keyword/Hashtag to search:")
nooftweet = int(input("Enter no. of tweet to analyze:"))
tweets = tweepy.Cursor(api.search,q=searchword,lang="English").items(nooftweet)

#declaring the variable
positive = 0
negative = 0
neutral = 0
polarity = 0

#reading the tweets and analyzing it
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0.00):
        neutral += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
        
#defining the function to calculate the percentage 
def percentage(part,whole):
    return 100 * float(part)/float(whole)
    
#calculate the percentage
positivep = percentage(positive,nooftweet)
negativep = percentage(negative,nooftweet)
neutralp = percentage(neutral,nooftweet)

#printing the results
print("The Overall Review on " + str(searchword) + " by Analyzing " + str(nooftweet) + " tweets")
if(positivep > negativep):
    print("positive")
elif(positivep > neutral):
    print("positive")
elif(neutralp > negativep):
    print("neutral")
else:
    print("negativep")
    
#data visulization using piechart
import matplotlib.pyplot as plt

labels = 'negative','neutral','positive'
sizes = [negativep,neutralp,positivep]
cols = ['c','m','r']
plt.pie(sizes,labels=labels,colors=cols,startangle=90,shadow=True,autopct='%1.1f%%')    
plt.legend()
plt.title("Overall Sentiment of the people in analzing "+ str(nooftweet) +" tweets")
plt.show()














