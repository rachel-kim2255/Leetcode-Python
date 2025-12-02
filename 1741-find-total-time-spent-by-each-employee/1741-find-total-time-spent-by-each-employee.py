import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id']).agg(
        total_time = ('total_time', sum)
    ).reset_index()
    employees = employees.rename(columns={'event_day':'day'})
    return employees.sort_values('emp_id', ascending=True)