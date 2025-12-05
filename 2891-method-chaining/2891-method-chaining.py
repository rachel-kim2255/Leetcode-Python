import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals
    return df[df['weight']>100].sort_values('weight', ascending=False)[['name']]
    