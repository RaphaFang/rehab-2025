import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = ((employees['employee_id'] & 1) ==1) & (employees['name'].str[0]!="M")
    employees["bonus"] = employees['salary'].where(condition,0)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    
# 要換個思路，將篩選結果作為一條件，或是一欄位
# 再基於這依據回吐
# employees["bonus"] 這樣可以建立欄位
