

SELECT unique_id, name
FROM Employees 
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id

SELECT euni.unique_id AS id, e.name AS user_name
FROM Employees e
LEFT JOIN EmployeeUNI euni
ON e.id = euni.id;
