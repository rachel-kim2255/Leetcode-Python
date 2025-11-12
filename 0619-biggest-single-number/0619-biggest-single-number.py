import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:    
    counting = my_numbers['num'].value_counts().reset_index()
    counting.columns = ['num', 'count']
    counting = counting[counting['count'] == 1]
    
    if counting.empty:
        return pd.DataFrame({'num': [None]})
    else:
        return pd.DataFrame({'num': [counting['num'].max()]})
    
    