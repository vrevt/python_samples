CREATE TABLE products (
 product_no integer,
 name text,
 price numeric CHECK (price > 0)
);

CREATE TABLE products (
 product_no integer,
 name text,
 price numeric CONSTRAINT positive_price CHECK (price > 0)
);

CREATE TABLE products (
 product_no integer NOT NULL,
 name text NOT NULL,
 price numeric
);

CREATE TABLE products (
 product_no integer NOT NULL,
 name text NOT NULL,
 price numeric NOT NULL CHECK (price > 0)
);

CREATE TABLE products (
 product_no integer UNIQUE,
 name text,
 price numeric
);

CREATE TABLE example (
 a integer,
 b integer,
 c integer,
 UNIQUE (a, c)
);