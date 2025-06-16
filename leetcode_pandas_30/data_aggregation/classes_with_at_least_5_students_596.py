import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby(['class']).agg({'student':"size"}).reset_index()  # where() 不能加在這，會變成不是df，導致錯誤
    return result.where(result['student'] >= 5).dropna()[['class']]
# pd的 groupby不會包含 被分類者的col
# 要透過 .reset_index() 還原

# agg({'student': 'size'})：計算每個 group 的資料筆數（就算 student 欄位有 NaN 也會算）
# .where(...).dropna()：先保留符合條件的，其他設成 NaN，再丟掉 NaN 列
# 較靈活，但較慢，因為多了一層 NaN 處理（memory/運算 overhead）


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby(['class']).count().reset_index()
    return result[result['student'] >= 5][['class']]
# .count()：針對每個欄位計數，不包含 NaN
# result['student'] >= 5：布林篩選，效能高，語意直觀
# 執行速度通常較快，適合你這種簡單統計 + 篩選情境

# .size() 會算 5 → 因為不管有沒有 NaN
# .count() 只會算非 NaN → 比如 Math 就變 3