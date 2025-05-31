import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    r = views[views['author_id']== views['viewer_id']][['author_id']]
    return r.drop_duplicates().sort_values(by='author_id').rename(columns={'author_id':'id'})

# .sort_values(by='author_id')
# 如果是Series，不用特別說特定哪一欄位，因為我這邊只有一個
# 但是是dataframe 就要

# 我這邊回傳是dataframe 就要