import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salary = employee['salary'].drop_duplicates().sort_values(ascending = False)
    
    if N <= 0 or N > len(distinct_salary):
        nth_salary = None
    else:
        nth_salary = distinct_salary.iloc[N-1]
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_salary]})