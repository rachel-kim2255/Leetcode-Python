import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals
    df['name'] = df['name'].astype(str)
    df= df[df['weight'] > 100]
    return df.sort_values('weight', ascending=False)[['name']]

    