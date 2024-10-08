SELECT g.name AS group_name, AVG(gd.grade) AS average_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gd ON s.id = gd.student_id
WHERE gd.subject_id = 5
GROUP BY g.id
ORDER BY average_grade DESC;
