import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge = employee.merge(employee, how='inner', left_on = 'managerId', right_on='id', suffixes=['_emp', '_mgr'])
    filtered = merge[merge['salary_emp'] > merge['salary_mgr']]
    return filtered.rename(columns={'name_emp':'Employee'})[['Employee']]

