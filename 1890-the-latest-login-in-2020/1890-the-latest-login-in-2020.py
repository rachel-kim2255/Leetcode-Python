import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins['time_stamp'] = pd.to_datetime(logins['time_stamp']) # it's already date time
    df = logins[logins['time_stamp'].dt.year == 2020]
    
    df = df.groupby('user_id')['time_stamp'].max().reset_index()
    df = df.rename(columns={'time_stamp':'last_stamp'})
    return df
