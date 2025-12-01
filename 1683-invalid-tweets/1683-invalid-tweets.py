import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['length'] = tweets['content'].str.len()
    tweets = tweets[tweets['length']> 15]
    return tweets[['tweet_id']]