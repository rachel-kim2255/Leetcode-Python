# LEARN: numpy - np.where / lambda - apply()
import pandas as pd

# 1. lambda, apply()
# def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['bonus'] = employees.apply(
#         lambda row: row['salary']
#                 if(row['employee_id'] % 2 != 0 and row['name'][0] != 'M')
#                 else 0,
#         axis =1
#     )
#     return employees[['employee_id', 'bonus']].sort_values('employee_id')

# 2. numpy, np.where
import numpy as np
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M')
    employees['bonus'] = np.where(
        condition,
        employees['salary'],
        0
    )

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')