SELECT
    name,
    elevation,
    sum(population)
FROM
    cities
GROUP BY
    GROUPING SETS ((name), (elevation), ());