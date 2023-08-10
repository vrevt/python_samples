CREATE TABLE people (
 height_cm numeric,
 height_in numeric GENERATED ALWAYS AS (height_cm / 2.54) STORED
);

insert into people (height_cm) values (1), (100);

select * from people;