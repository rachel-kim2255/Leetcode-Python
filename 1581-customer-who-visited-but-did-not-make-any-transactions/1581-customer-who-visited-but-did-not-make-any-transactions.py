import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = visits.merge(transactions, on='visit_id', how='left')
    no_trans = merged[merged['transaction_id'].isna()]
    result = no_trans.groupby('customer_id').size().reset_index(name='count_no_trans')
    return result
