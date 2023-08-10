CREATE TABLE cities (
 name text,
 population real,
 elevation int -- (in ft)
);

CREATE TABLE capitals (
 state char(2) UNIQUE NOT NULL
) INHERITS (cities);


-- another samples
table people;

CREATE TABLE cities (
 name text,
 population float,
 elevation int -- in feet
);
CREATE TABLE capitals (
 state char(2)
) INHERITS (cities);

create table historical_capitals (
    famous text
) inherits (capitals);

insert into cities (name, population, elevation) values ('minsk', 1000000, 300);
insert into historical_capitals (name, population, elevation, state, famous) values ('ele', 1000, 300, 'ru', 'fsfnosfhof');

select * from only cities;
select * from historical_capitals;

SELECT p.relname ,c.tableoid, c.name, c.elevation
FROM cities c, pg_class p
where c.TABLEOID = p.oid;

SELECT c.tableoid::regclass, c.name, c.elevation
FROM cities c;
