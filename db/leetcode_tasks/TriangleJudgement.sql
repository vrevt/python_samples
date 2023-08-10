Create table If Not Exists Triangle (x int, y int, z int);
Truncate table Triangle;
insert into Triangle (x, y, z) values ('13', '15', '30');
insert into Triangle (x, y, z) values ('10', '20', '15');


select
    x,
    y,
    z,
    case
        when x >= y and x >= z and x < y + z then 'YES'
        when y >= z and y >= x and y < z + x then 'YES'
        when z >= x and z >= y and z < x + y then 'YES'
        else 'NO'
    end as triangle
from
    Triangle
