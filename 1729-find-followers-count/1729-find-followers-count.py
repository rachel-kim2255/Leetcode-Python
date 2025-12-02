import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    followers = followers.groupby('user_id')[['follower_id']].nunique().reset_index()
    followers=followers.rename(columns={'follower_id':'followers_count'})
    return followers
    