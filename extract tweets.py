# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:07:37 2018

@author: HP
"""
import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "Sh4rtCV78EummAG1yWaQaXmyw" 
consumer_secret = "h6BTyRKOKPol7ucXiZRNmiJuFTM4wvsu8adIU5rt5qVy6N6TfX"
access_key = "1046769984737665029-y7HJ9s9wBEyDkJKHc5ik3CCyX083Q3"
access_secret = "j51htadkbtPBkuiL46ZlWp1fB7tlXREia32UarRH5WKAv"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=2
        tweets = api.user_timeline(screen_name=username,count=number_of_tweets) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("@PratyushGarg9")  
