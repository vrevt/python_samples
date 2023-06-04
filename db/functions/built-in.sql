select repeat('aba', 5) as rep;

select abs(-5);

select cbrt(64);

select sqrt(9);

select ceil(42.1); --round up

select floor(42.9); --round down

select round(42.49, 0); --math round

select trunc(23.9);

select div(5, 2);

select factorial(5);

select gcd(1071, 462);

select lcm(1071, 462);

select random(); --[0..1)

select lower('aBcD');

select upper('asjdlaf');

select starts_with('abcde', 'ab');

select position('om' in 'Thomas');

select ascii('x');

select chr(120);

select concat('abcde', 2, NULL, 22);

select left('abcdesfjlfs', 2);

select right('abcdesfjlfs', 2);

select length('anc');

select age(timestamp '2001-04-10', timestamp '1957-06-13');

select clock_timestamp ();

select date_part('hour', clock_timestamp());

SELECT EXTRACT(CENTURY FROM TIMESTAMP '2000-12-16 12:21:13');
SELECT EXTRACT(isodow FROM TIMESTAMP '2023-06-04 20:38:40');

SELECT date_trunc('hour', TIMESTAMP '2001-02-16 20:38:40');
-- Result: 2001-02-16 20:00:00

SELECT date_trunc('year', TIMESTAMP '2001-02-16 20:38:40');
-- Result: 2001-01-01 00:00:00

select timestamp '2001-02-16 20:38:40' at time zone 'GMT';

SELECT pg_sleep(30);
-- time sleep 30 sec
