import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated = person.groupby('email').size().reset_index(name='count')
    duplicated = duplicated[duplicated['count'] > 1][['email']]
    duplicated.columns = ['Email']
    return duplicated
