import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[cinema['description'] != 'boring']
    cinema = cinema[cinema['id'] % 2 == 1]
    cinema = cinema.sort_values(by = 'rating', ascending= False)
    cinema = pd.DataFrame(cinema)
    return cinema
    
    