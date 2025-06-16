import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    else:
        r = orders.groupby(['customer_number']).count().reset_index().rename(columns={'order_number':'cnt'})
        return r.loc[[r['cnt'].idxmax()]][['customer_number']]


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    j = orders['customer_number'].mode()   
    return pd.DataFrame({'customer_number': j})

# orders['cnt'] = orders.groupby(['customer_number']).count()...
# 可以這樣把數值放回原先的 table 但會出現一問題
# 資料會混在一起，舊排列數據，會跟新排列一起出現

# ! df or series
# r.loc[[r['cnt'].idxmax()]] -> 這會給我df
# r.loc[r['cnt'].idxmax()] -> 這會給我series

# 要建立 df
# pd.DataFrame(columns=['customer_number']) -> 需要這樣寫
# pd.DataFrame(columns='customer_number') -> 這樣會報錯

# mode 或許是更快的方式