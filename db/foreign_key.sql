CREATE TABLE orders (
 order_id integer PRIMARY KEY,
 product_no integer REFERENCES products (product_no),
 quantity integer
);

CREATE TABLE t1 (
 a integer PRIMARY KEY,
 b integer,
 c integer,
 FOREIGN KEY (b, c) REFERENCES other_table (c1, c2)
);