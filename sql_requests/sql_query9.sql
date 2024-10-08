select distinct s.name
from subjects s
join grades g on g.subject_id = s.id
join students st on st.id = g.student_id
where st.id = 2
limit 5;