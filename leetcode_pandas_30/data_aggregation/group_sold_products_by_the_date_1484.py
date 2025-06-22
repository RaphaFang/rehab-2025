import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return (activities
            .groupby("sell_date", as_index=False)
            .agg(
                num_sold = ("product","nunique"),
                products = ("product", lambda x: ",".join(sorted(x.unique())))
            ))


# --------------------------------------------------------------------------------
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    r = (activities
         .drop_duplicates()
         .groupby("sell_date", as_index=False)
         .agg(
             num_sold = ('product', 'count'),
             products = ('product', lambda x: ','.join(sorted(x)))
         ))
    return r

# --------------------------------------------------------------------------------
# 下面的寫法會快一點
# 因為，drop_duplicates() 下面只做一次，但是上面做了兩次，分別在agg()裡面的兩個欄位

# 要統一寫agg()的方式，先命名欄位，接著傳入舊欄位，以及希望施加的函數