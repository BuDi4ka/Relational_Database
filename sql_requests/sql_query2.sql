select s.name, avg(g.grade) as avg_grade
from students s
join grades g on s.id = g.student_id
where g.subject_id = 2
group by s.id
limit 1;