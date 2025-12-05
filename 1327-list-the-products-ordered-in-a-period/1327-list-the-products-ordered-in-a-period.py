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




    # orders['order_date'] = pd.to_datetime(orders['order_date'])

    # # 1) 2020년 2월만 필터링
    # mask = (
    #     (orders['order_date'] >= '2020-02-01') &
    #     (orders['order_date'] <= '2020-02-29')
    # )
    # orders_feb = orders[mask]

    # # 2) products와 merge
    # merged = orders_feb.merge(products, on='product_id', how='inner')

    # # 3) product별로 unit 합계
    # grouped = (
    #     merged.groupby(['product_id', 'product_name'])['unit']
    #         .sum()
    #         .reset_index()
    # )

    # # 4) 100개 이상 주문된 제품만
    # result = grouped[grouped['unit'] >= 100]

    # print(result)
        
    



