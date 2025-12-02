import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, how='left', left_on='managerId', right_on='id')
    filtered = (employee['managerId_x'] != 'null') & (employee['salary_x'] > employee['salary_y'])
    employee = employee[filtered]
    employee = employee.rename(columns = {'name_x': 'Employee'})
    return employee[['Employee']]
  

