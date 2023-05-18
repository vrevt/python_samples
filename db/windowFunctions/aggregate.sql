select
    name,
    subject,
    grade,
    sum(grade) over (partition by name) as sum_grade,
    avg(grade) over (partition by name) as avg_grade,
    count(grade) over (partition by name) as count_grade,
    min(grade) over (partition by name) as min_grade,
    max(grade) over (partition by name) as max_grade
from student_grades;