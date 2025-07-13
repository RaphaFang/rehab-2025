SELECT user_id, CONCAT(Upper(LEFT(name, 1)), Lower(SUBSTRING(name,2))) as name
from Users;