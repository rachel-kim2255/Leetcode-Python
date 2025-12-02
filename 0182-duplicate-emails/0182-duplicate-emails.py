import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # df = person.groupby('email')['email'].agg(
    #     count = 'count'
    # ).reset_index()
    # df = df[df['count'] > 1]
    # df = df.rename(columns={'email':'Email'})
    # return df[['Email']]

#    (각 행에 해당 이메일의 총 개수를 붙여주는 역할)
    email_counts = person.groupby('email')['email'].transform('count')
    
    # 2. 필터링: 개수가 1보다 큰 (중복된) 행만 남깁니다.
    duplicates = person[email_counts > 1]
    
    # 3. 최종 반환: 'email' 컬럼만 선택한 후, 중복된 행을 제거하고 반환합니다.
    return duplicates[['email']].drop_duplicates()


