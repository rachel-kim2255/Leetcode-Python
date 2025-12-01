# LEARN:
# 1. nunique() -> count all users
# 2. count each contest's participants using nunique()
# 3. calculate percentage

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    total_users = users['user_id'].nunique()
    counted = register.groupby('contest_id')['user_id'].nunique().reset_index()
    counted['percentage'] = (counted['user_id'] / total_users * 100).round(2)
    return counted[['contest_id', 'percentage']].sort_values(['percentage', 'contest_id'], ascending=[0,1])
