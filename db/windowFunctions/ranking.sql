select
    name,
    subject,
    grade,
    row_number() over (partition by name order by grade desc) as rn,
    rank() over (partition by name order by grade desc) as r,
    dense_rank() over (partition by name order by grade desc) as dr
from student_grades;



select
    Department,
    employee,
    salary
from (select
          d.name as Department,
          e.name as employee,
          e.salary,
          DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS drk
      from
          Employee e
          join Department d on e.DepartmentId = d.Id
     ) t
where
    t.drk <= 3;