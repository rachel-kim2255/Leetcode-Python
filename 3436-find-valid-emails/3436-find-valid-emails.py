import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    regex_pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$"
    condition = users['email'].str.match(regex_pattern, na=False)
    valid_users = users[condition]

    result = valid_users.sort_values(by='user_id', ascending=True)

    return result

    