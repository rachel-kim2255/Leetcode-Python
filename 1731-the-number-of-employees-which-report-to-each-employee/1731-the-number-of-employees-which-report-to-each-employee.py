import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employees, how='inner', left_on='employee_id', right_on='reports_to')
    employees = employees.groupby(['employee_id_x', 'name_x']).agg(
        reports_count = ('employee_id_y', 'count'),
        average_age= ('age_y', 'mean')
    ).reset_index()
    employees = employees.rename(columns={'employee_id_x':'employee_id', 'name_x':'name'})
    #employees['average_age'] = np.ceil(employees['average_age'])
    employees['average_age'] = (employees['average_age']+ 1e-9).round().astype('int')
    return employees
    