# LEARN:
# pd.to_datetime() → converts a string into a datetime object
# shift(1) → retrieves the value from the previous row
# result = weather[(Condition A) & (Condition B)][['id']] → keeps only the rows that meet both conditions, and extracts the id column in a DataFrame format

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_date'] = weather['recordDate'].shift(1)

    result = weather[
        ((weather['recordDate'] - weather['prev_date']).dt.days == 1) &
        (weather['temperature'] > weather['prev_temp'])
    ][['id']]

    return result
