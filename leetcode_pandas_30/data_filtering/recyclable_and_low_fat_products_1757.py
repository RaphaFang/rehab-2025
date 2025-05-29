import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"]=='Y') & (products["recyclable"]=='Y')][["product_id"]]

# 要注意，後面的[[]]是套兩層，才會傳回Dataframe

# SELECT product_id
# FROM Products
# where low_fats = 'Y'
#     AND recyclable = 'Y';

