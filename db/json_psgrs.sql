SELECT *
FROM
ROWS FROM
 (
 json_to_recordset('[{"a":40,"b":"foo"}, {"a":"100","b":"bar"}]') AS (a INTEGER, b TEXT),
 generate_series(1, 3)
 ) AS x (p, q, s)
ORDER BY p;