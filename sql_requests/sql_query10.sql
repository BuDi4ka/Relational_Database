select s.name, sb.name, t.name
from students s
join grades g on g.student_id = s.id
join subjects sb on g.subject_id = sb.id
join teachers t on t.id = sb.teacher_id
where t.id = 2
and s.id = 10

