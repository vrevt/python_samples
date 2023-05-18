select
    name,
    subject,
    grade,
    row_number() over (partition by name order by grade desc) as rn,
    rank() over (partition by name order by grade desc) as r,
    dense_rank() over (partition by name order by grade desc) as dr
from student_grades;