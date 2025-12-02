import pandas as pd
# 181. Employees Earning More Than Their Managers
# def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
#     employee = employee.merge(employee, how='left', left_on='managerId', right_on='id')
#     filtered = (employee['managerId_x'] != 'null') & (employee['salary_x'] > employee['salary_y'])
#     employee = employee[filtered]
#     employee = employee.rename(columns = {'name_x': 'Employee'})
#     return employee[['Employee']]
  
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 매니저 ID를 키로 하여 Self Join
    merged_df = employee.merge(employee, how='inner', left_on='managerId', right_on='id', suffixes=['_emp', '_mgr'])
    
    # 1. 직원 급여(salary_emp)가 매니저 급여(salary_mgr)보다 큰 경우만 필터링
    filtered_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]
    
    # 2. 컬럼 이름 변경 및 최종 반환
    return filtered_df.rename(columns={'name_emp': 'Employee'})[['Employee']]

# 참고: Inner Join (how='inner')을 사용하면 매니저가 없는 직원(CEO)은 
# 애초에 Merge 대상이 아니므로 자동으로 제외됩니다.
