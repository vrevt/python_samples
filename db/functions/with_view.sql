CREATE TABLE foo (fooid int, foosubid int, fooname text);

insert into foo (fooid, foosubid, fooname) values
                                               (1, 1, 'apple'),
                                               (2, 2, 'egg'),
                                               (3, 3, 'pumpkin'),
                                               (1, 1, 'potato');

CREATE FUNCTION getfoo(int) RETURNS SETOF foo AS $$
 SELECT * FROM foo WHERE fooid = $1;
$$ LANGUAGE SQL;

SELECT * FROM getfoo(2) AS t1;

SELECT
    *
FROM
    foo
WHERE foosubid IN (
    SELECT
        foosubid
    FROM
        getfoo(foo.fooid) z
    WHERE
        z.fooid = foo.fooid
    );

CREATE VIEW vw_getfoo AS SELECT * FROM getfoo(1);

select * from vw_getfoo;