import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    counting = daily_sales.groupby(['date_id', 'make_name'],as_index=False).nunique(['lead_id', 'partner_id'])
    counting= counting.rename(columns={'lead_id':'unique_leads', 'partner_id':'unique_partners'})
    
    return counting
    