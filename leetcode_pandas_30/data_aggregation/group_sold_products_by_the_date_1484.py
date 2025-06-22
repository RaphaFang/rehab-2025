import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby("sell_date")["product"].agg([
        ("num_sold","nunique"),
        ("products", lambda x: ",".join(sorted(x.unique())))
    ]).reset_index()

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    r = (activities
         .drop_duplicates()
        #  .sort_values('product')
         .groupby("sell_date", as_index=False)
         .agg(
             num_sold = ('product', 'count'),
             products = ('product', lambda x: ','.join(x))
         )
         .rename(columns = {'product':'num_sold'}))
    return r

