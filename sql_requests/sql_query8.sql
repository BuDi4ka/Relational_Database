select avg(g.grade)
from grades g
join subjects s on g.subject_id = s.id
join teachers t on s.teacher_id = t.id
where t.id = 2