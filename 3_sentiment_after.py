from __future__ import division
import urllib
import csv
from string import punctuation


files=['negative.txt','positive.txt','obama_tweets.txt']

path='https://raw.github.com/mjhea0/twitter-sentiment-python/master/words/'
for file_name in files:
    urllib.urlretrieve(path+file_name,file_name)


tweets = open("obama_tweets.txt").read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]


for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
    
    tweet_processed=tweet.lower()
    
    
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words and word != '':
            positive_counter=positive_counter+1
        elif word in negative_words and word != '':
            negative_counter=negative_counter+1
        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)


output=zip(tweets_list,positive_counts,negative_counts)

print len(positive_counts)

writer = csv.writer(open('tweet_sentiment_after.csv', 'wb'))
writer.writerows(output)