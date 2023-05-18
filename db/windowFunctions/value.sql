with

all_three_id as(
select 
    student_id
from 
    step_student 
    join step using(step_id)
where result='correct'
group by 1
having count(distinct lesson_id)=3
order by 1),

all_data as(
select
    student_id, 
    student_name as 'Студент',
    concat(module_id, '.', lesson_position) as 'Урок',
    from_unixtime(max(attempt_time) over (partition by student_id)) as 'Макс_время_отправки'
from
    all_three_id 
    left join student using(student_id)
    left join step_student using(student_id)
    left join step using(step_id)
    left join lesson using(lesson_id)
where 
    result = 'correct'
),

inerval as(
select
    Студент,
    Урок,
    Макс_время_отправки,
    ifnull(ceiling((Макс_время_отправки - lag(Макс_время_отправки) 
                    over (partition by student_id order by Макс_время_отправки))/86400), '-') as 'Интервал'
from all_data)
    
select * from interval;
 