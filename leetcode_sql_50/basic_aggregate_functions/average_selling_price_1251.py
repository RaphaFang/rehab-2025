import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    all_products_checklist = prices[['product_id']].drop_duplicates()

    if not units_sold.empty:
        cross = prices.merge(units_sold, on="product_id", how='outer')
        valid = cross[(cross['purchase_date'] >= cross['start_date']) & (cross['purchase_date'] <= cross['end_date'])]

        valid['revenue'] = valid['price'] * valid['units']

        sum = valid.groupby('product_id').agg({
            'revenue':'sum',
            'units':'sum'
        }).reset_index()


        sum['average_price'] = (sum['revenue'] / sum['units']).round(2)
        result = all_products_checklist.merge(sum[['product_id', 'average_price']], how='left', on='product_id')
        result['average_price'] = result['average_price'].fillna(0)

        return result
    
    return all_products_checklist.assign(average_price=0)



# 可以這樣理解reset_index
# 如果我用groupby，會得到基於product_id為index的DF，這時候我如果加上reset，且沒有drop，會將product_id往右推，變成一個col

# 注意
# 不論sql還是pd，他們的JOIN都是半Cartesian product
# 選定 'on'的欄位A有1,2,3，B有1[1.1,1.2],2[2.1,2.2]
# 會得到
# A'1 B1.1 
# A'1 B1.2
# A'2 B2.1
# A'2 B2.2
# A'3 null