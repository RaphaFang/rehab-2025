import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = (
        employees.groupby(['event_day','emp_id'], as_index=False)
        .agg({'total_time': 'sum'})
    ).rename(columns={'event_day':'day'})
    return result


    # print(result)


# +------------+--------+------------+
# | day        | emp_id | total_time |
# +------------+--------+------------+
# | 2020-11-28 | 1      | 173        |
# | 2020-11-28 | 2      | 30         |
# | 2020-12-03 | 1      | 41         |
# | 2020-12-09 | 2      | 27         |
# +------------+--------+------------+