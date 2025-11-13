# KEY: replace

import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].replace({'m': 'f', 'f':'m'})
    return salary

    # 2. lambda funciton
    # salary['sex'] = salary['sex'].apply(lambda x: 'f' if x == 'm' else 'm')
    # return salary



    