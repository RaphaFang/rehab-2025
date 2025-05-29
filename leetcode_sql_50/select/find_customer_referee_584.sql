SELECT name
FROM Customer
WHERE referee_id <> 2
    AND referee_id IS NULL;


-- WHERE referee_id !=2
-- WHERE referee_id <> 2