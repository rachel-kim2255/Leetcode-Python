import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    total_borrowed = borrowing_records[borrowing_records['return_date'].isna()].groupby(['book_id']).size().reset_index(name='current_borrowers')
    merged = library_books.merge(total_borrowed, on='book_id', how='left')
    result = merged[merged['total_copies'] == merged['current_borrowers']]
    return result.drop(columns='total_copies').sort_values(by=['current_borrowers', 'title'], ascending=[False, True])

    # df1 = library_books
    # df2 = borrowing_records
    
    # loans = df2[df2['return_date'].isna()]
    # counts = loans.groupby('book_id').size().reset_index(name='current_borrowers')

    # df = df1.merge(
    #     counts, 
    #     on='book_id', 
    #     how='left'
    # )
    
    # df['current_borrowers'] = df['current_borrowers'].fillna(0)
    # df['available_copies'] = df['total_copies'] - df['current_borrowers']
    # df = df[df['available_copies'] == 0].copy()
    # final_cols = ['book_id', 'title', 'author', 'genre', 'publication_year', 'current_borrowers']
    
    # return df[final_cols].sort_values(
    #     by=['current_borrowers', 'title'],
    #     ascending=[False, True]
    # )



    