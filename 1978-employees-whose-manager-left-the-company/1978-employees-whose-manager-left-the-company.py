# import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[employees['salary'] < 30000]
    df2 = df.merge(employees, how='left', left_on='manager_id', right_on='employee_id')
    
    condition = (df2['employee_id_y'].isna()) & (df2['manager_id_x'].notna())
    df2 = df2[condition]
    df2 = df2.rename(columns={'employee_id_x':'employee_id'})
    return df2[['employee_id']].sort_values('employee_id')
    
    # return df2[['employee_id']]

