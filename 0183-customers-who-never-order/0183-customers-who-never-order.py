# key: customers[~customers[id].isin(y_order)]
# learn: = customers[customers[id].isin(y_order) == False]

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    customers = customers[customers['id_y'].isna()]
    return customers.rename(columns={'name':'Customers'})[['Customers']]



    
