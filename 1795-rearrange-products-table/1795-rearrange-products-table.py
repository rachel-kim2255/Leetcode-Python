import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # 1. melt() 함수를 사용하여 데이터 언피봇팅 (Unpivoting)
    # id_vars: 그대로 유지할 ID 컬럼 (product_id)
    # value_vars: 행으로 변환할 컬럼들 ('price1', 'price2', 'price3')
    # var_name: 변환된 컬럼 이름을 저장할 새 컬럼 이름 ('store')
    # value_name: 변환된 값을 저장할 새 컬럼 이름 ('price')
    df = products.melt(
        id_vars = ['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )
    df2 = df.dropna(subset=['price'])

    return df2.sort_values('store', ascending=True)


    
    # # 2. 가격(price)이 NaN (SQL의 NULL에 해당)인 행 제거
    # result_df = melted_df.dropna(subset=['price'])
    
    # # 3. 'store' 컬럼 값 정리: 'price1'을 'store1'로 변경 (선택 사항)
    # # 요구사항에 더 정확하게 맞추기 위해 'price' 접두사를 'store'로 대체합니다.
    # result_df['store'] = result_df['store'].str.replace('price', 'store')
    
    # # 4. 최종적으로 필요한 컬럼 순서로 반환
    # return result_df[['product_id', 'store', 'price']]