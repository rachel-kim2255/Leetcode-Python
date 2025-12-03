import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(salaries, how='outer', on='employee_id')
    df = df[(df['name'].isna()) | (df['salary'].isna())]
    return df[['employee_id']]
    