SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) as attended_exams

FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id;

-- cross
-- 可以讓你到全部的排列，但是前提是你的SELECT要選對
-- 如果選到有空缺的表的col，得到的會是有null的
-- sub.subject_name 我錯誤的選到e.subject_name，就會是有洞的
