import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    temp =  (activity.sort_values(by='event_date')
             .groupby('player_id',as_index=False)
             .first()
             )[['player_id', 'event_date']]

    return temp.rename(columns={'event_date':'first_login'})

# 如果先groupby,就不能 sort
# AttributeError: 'DataFrameGroupBy' object has no attribute 'sort_values'
    # return activity.groupby('player_id',as_index=False).sort_values(by='event_date').head(1)[['player_id', 'event_date']]
    
# .groupby('player_id',as_index=False)
# 沒有加上as_index，境會讓你的groupby變成新的index