import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby(['teacher_id'], as_index = False).agg({'subject_id':'nunique'}).rename(columns={'subject_id':'cnt'})
    # print(teacher)
    return teacher[['teacher_id', 'cnt']]