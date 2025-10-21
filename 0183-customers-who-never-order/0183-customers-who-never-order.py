# key: customers[~customers[id].isin(y_order)]
# learn: = customers[customers[id].isin(y_order) == False]

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    y_order = orders['customerId'].unique()
    n_order = customers[~customers['id'].isin(y_order)]
    n_order = n_order[['name']]
    n_order.columns = ['Customers']
    
    return n_order



    
