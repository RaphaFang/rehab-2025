import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    r = customers.merge(orders, how='left',left_on='id',right_on='customerId')
    r = r[r['customerId'].isnull()][['name']]
    return r.rename(columns={'name':'Customers'})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    r = customers[~customers['id'].isin(orders['customerId'])][['name']]
    return r.rename(columns={'name': 'Customers'})