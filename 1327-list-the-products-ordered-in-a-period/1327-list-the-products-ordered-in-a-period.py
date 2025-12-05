import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    condition = (
        (orders['order_date'] >= '2020-02-01') &
        (orders['order_date'] <= '2020-02-29')
    )
    feb = orders[condition]
    feb = feb.groupby('product_id')['unit'].sum().reset_index()

    merge = products.merge(feb, how='left', on='product_id')
    merge = merge[merge['unit']>= 100]
    return merge[['product_name', 'unit']]
