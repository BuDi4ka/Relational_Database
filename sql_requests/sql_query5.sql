select s.name
from subjects s
join teachers t on t.id = s.teacher_id
where teacher_id = 2
