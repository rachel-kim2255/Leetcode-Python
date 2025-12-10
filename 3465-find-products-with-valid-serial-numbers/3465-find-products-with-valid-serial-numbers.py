import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    serial = r'.*\bSN\d{4}-\d{4}\b.*'
    filtered = products['description'].str.contains(serial, regex=True)
    products = products[filtered]
    return products.sort_values('product_id')



    