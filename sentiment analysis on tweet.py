
import tweepy 
import json
from watson_developer_cloud import ToneAnalyzerV3
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""
  
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
        return tmp[0] 
    


tone_analyzer = ToneAnalyzerV3(
    version='',
    username='',
    password='',
    url=''
)

text = get_tweets("@PratyushGarg9")

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))    
