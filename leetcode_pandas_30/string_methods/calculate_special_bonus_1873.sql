-- import pandas as pd

-- def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
--     condition = ((employees['employee_id'] & 1) ==1) & (employees['name'].str[0]!="M")
--     employees["bonus"] = employees['salary'].where(condition,0)
--     return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    


SELECT employee_id,
    CASE
        WHEN MOD(employee_id, 2) =1 AND name not LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM Employees 
ORDER BY employee_id;

-- MOD(employee_id, 2)
-- 這是算餘數的