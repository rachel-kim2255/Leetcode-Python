# LEARN: 
# 1. calculate amount by account (balance)
# 2. filter: balance > 10000
# 3. merge and change the name

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balance = transactions.groupby('account')['amount'].sum().reset_index()
    balance = balance[balance['amount']>10000]
    df = balance.merge(users, on = 'account', how = 'left')
    df= df.rename(columns={'name':'NAME', 'amount':'BALANCE'})
    df = df[['NAME', 'BALANCE']]
    return df


