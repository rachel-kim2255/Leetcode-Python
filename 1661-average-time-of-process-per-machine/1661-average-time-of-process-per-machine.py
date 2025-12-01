# LEARN:
# 1. Seperate 'start' & 'end'
# 2. merge them and calculate the time 

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start = activity[activity['activity_type'] == 'start']
    end = activity[activity['activity_type'] == 'end']
    df = start.merge(end, on=['machine_id', 'process_id'])
    df['time'] = df['timestamp_y'] - df['timestamp_x']
    df = df.groupby('machine_id')['time'].mean().round(3).reset_index()
    df=df.rename(columns={'time':'processing_time'})
    return df