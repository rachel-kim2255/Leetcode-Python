import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    email_counts = person.groupby('email')['email'].transform('count')
    dup = person[email_counts > 1]
    return dup[['email']].drop_duplicates()


