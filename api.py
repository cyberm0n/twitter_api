import time
start_time = time.time()

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "bitcoin"
tweets = []
limit = 100000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else: 
        tweets.append([tweet.date,tweet.username,tweet.content])

df = pd.DataFrame(tweets,columns=["Date","User","Tweet"])

df.to_csv("twit.csv")

print("--- %s seconds ---" % (time.time() - start_time))
