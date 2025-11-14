# LEARN: pivot
# PROCESS: pivot - complete columns - reset_index()
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    df = department.pivot(index='id', columns ='month', values='revenue')
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    df = df.reindex(columns=months)
    df.columns = [f"{m}_Revenue" for m in df.columns]
    df = df.reset_index()
    return df
    
