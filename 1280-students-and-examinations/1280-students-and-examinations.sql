# Write your MySQL query statement below
select
    students.student_id,
    student_name,
    subjects.subject_name,
    count(examinations.student_id) as attended_exams
from students
cross join subjects
left join examinations
    on students.student_id = examinations.student_id
    and subjects.subject_name = examinations.subject_name
group by 1, 2, 3
order by 1, 3