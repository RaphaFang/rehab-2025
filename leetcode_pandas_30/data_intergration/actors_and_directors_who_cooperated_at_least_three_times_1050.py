import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    r = (actor_director
         .groupby(['actor_id', 'director_id'], as_index=False)
         .agg(
             counter = ('timestamp', 'count')
         ))
    return r[r['counter'] >= 3][['actor_id','director_id']]

# 用 as_index 。可讀性佳：回傳就是標準 DataFrame，不是 MultiIndex。
# 用 r[r['counter'] >= 3]。不用要 where
# 前這是 numpy加速

# ------------------------------------------------------------------------------
# 寫 size() 會略快

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    r = (actor_director
     .groupby(['actor_id', 'director_id'])
     .size()
     .reset_index(name='counter'))
    return r[r['counter'] >= 3][['actor_id', 'director_id']]