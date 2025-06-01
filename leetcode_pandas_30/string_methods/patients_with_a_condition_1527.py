import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    regex = r'(^| )DIAB1'  # 他只能是開頭或是空格
    return patients[patients['conditions'].str.contains(regex)] 

# 不能用match，因為match 會強制轉換成檢測開頭