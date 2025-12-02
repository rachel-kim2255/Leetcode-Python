import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email')['email'].agg(
        count = 'count'
    ).reset_index()
    df = df[df['count'] > 1]
    df = df.rename(columns={'email':'Email'})
    return df[['Email']]



