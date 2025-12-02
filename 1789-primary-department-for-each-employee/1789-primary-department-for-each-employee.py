# import pandas as pd

# def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
#     result = employee[employee['primary_flag'] == 'Y']
#     count_id = employee['employee_id'].value_counts()
#     result2 = employee[employee['employee_id'].map(count_id) == 1]
#     result_df = pd.concat([result, result2], ignore_index=True)
#     return result_df[['employee_id', 'department_id']]

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    dept_counts = employee.groupby('employee_id')['department_id'].transform('count')
    final = (employee['primary_flag'] == 'Y') | (dept_counts == 1)
    result = employee[final]
    
    return result[['employee_id', 'department_id']]