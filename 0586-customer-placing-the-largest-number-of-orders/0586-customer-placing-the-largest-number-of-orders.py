import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_count = orders.groupby('customer_number').size().reset_index(name = 'counted')
    max_order = order_count['counted'].max()
    result = order_count[order_count['counted'] == max_order][['customer_number']]
    
    return result
