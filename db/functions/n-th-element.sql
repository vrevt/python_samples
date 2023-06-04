CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (select
              salary
          from (select
                    e.salary,
                    dense_rank() over (order by e.salary desc) drk
                from
                    Employee e
                ) tmp
          where drk = N
          group by 1
  );
END