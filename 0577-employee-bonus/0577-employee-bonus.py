import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    employee_info = pd.merge(employee, bonus, on='empId', how='left')
    employee_info = employee_info[
        (employee_info['bonus'] < 1000) | (employee_info['bonus'].isnull())
        ][['name', 'bonus']]
    return employee_info

