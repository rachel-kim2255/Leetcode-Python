import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return products[['product_id']]
    
    # 2. Method Chaining
    # return products[
    #     (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    # ][['product_id']]