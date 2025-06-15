import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby(['class']).agg({'student':"size"}).reset_index()  # where() 不能加在這，會變成不是df，導致錯誤
    return result.where(result['student'] >= 5).dropna()[['class']]

# pd的 groupby不會包含 被分類者的col
# 要透過 .reset_index() 還原