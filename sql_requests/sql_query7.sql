select s.name, g.grade
from grades g
join students s on g.student_id = s.id
where g.subject_id = 3
and s.group_id = 1