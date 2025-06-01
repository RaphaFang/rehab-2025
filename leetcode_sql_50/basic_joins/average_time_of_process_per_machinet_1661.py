# SELECT a.machine_id, ROUND(AVG(a.timestamp - b.timestamp),3) AS processing_time
# FROM Activity a
# JOIN Activity b
#     ON a.machine_id = b.machine_id AND a.process_id = b.process_id
# WHERE a.activity_type = 'start' AND b.activity_type = 'end'
# GROUP BY a.machine_id;

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    a = activity[activity['activity_type'] == 'start']
    b = activity[activity['activity_type']=='end']
    count = a.merge(b,on=['machine_id','process_id'],suffixes=['_a','_b'])

    count['processing_time'] = count['timestamp_b'] - count['timestamp_a']
    return count.groupby('machine_id')['processing_time'].mean().round(3).reset_index()

    # 要注意，我透過count.groupby()，這時我的資料只是series，並且只有machine_id，跟count計算出的數值
    # 一定要透過reset_index 轉換成DF
    # result.columns = ['machine_id','processing_time']


# 下面我完全看不懂
def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    pivot_df = activity.pivot_table(index=['machine_id', 'process_id' ], columns='activity_type', values = 'timestamp')
    pivot_df['dur'] = round(pivot_df['end'] - pivot_df['start'],3)
    return pivot_df.groupby('machine_id')['dur'].mean().round(3).reset_index(name='processing_time')


    