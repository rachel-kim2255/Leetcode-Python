# Learn: If you use 'merge' with the condition != 'RED', 
# the result fails to exclude salespersons who have worked with both RED and other companies. 
# (The record of RED will be removed, but their other records will remain.)


import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_ids = company[company['name'] == 'RED']['com_id']
    red_sales = orders[orders['com_id'].isin(red_ids)]['sales_id']
    result = sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]
    return result




# def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     sales = pd.merge(orders, company,on='com_id', how='left')
#     sales2= pd.merge(sales, sales_person, on = 'sales_id', how='left', suffixes=('_company', '_sales'))
#     sales2 = sales2[sales2['name_company'] != 'RED']
#     sales2= sales2.rename(columns={'name_sales':'name'})
#     sales2=sales2['name']
#     return pd.DataFrame(sales2)