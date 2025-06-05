import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, 
            id_vars='product_id',value_vars=['store1', 'store2', 'store3'],
            var_name='store', value_name='price').dropna()


# wide form, long form


# ! sql沒有melt()，要透過 UNION ALL
# mysql 沒有 UNPIVOT ，所以要透過 UNION ALL 模擬
# SELECT product_id, 'store1' AS store, store1 AS price
# FROM Products
# WHERE store1 IS NOT NULL

# UNION ALL

# SELECT product_id, 'store2' AS store, store2 AS price
# FROM Products
# WHERE store2 IS NOT NULL

# UNION ALL

# SELECT product_id, 'store3' AS store, store3 AS price
# FROM Products
# WHERE store3 IS NOT NULL;
