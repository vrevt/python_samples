create table mvcctable
(
	idcol integer,
	valcol char (255)
) with (autovacuum_enabled = off);

create index idx_mvcctable on mvcctable (idcol);


insert into mvcctable (idcol, valcol)
select *, substr (md5 (random ()::text), 0, 255)
from generate_series (1, 100000);

select count(*) from mvcctable;

select
	tableoid,
	xmin,
	xmax,
	ctid,
	*
from
	mvcctable;

select pg_size_pretty(pg_relation_size('mvcctable'));


begin;
update mvcctable
set valcol = 'newvalue'
where idcol <= 100;

select *
from mvcctable
where idcol <= 100;

commit;



select
	relname as tablename,
	n_live_tup as livetuples,
	n_dead_tup as deadtuples
from
	pg_stat_user_tables
where
	relname = 'mvcctable';



update	mvcctable
set	valcol = 'MassiveUpdate'
where	idcol <= 50000;


select pg_size_pretty(pg_relation_size('mvcctable'));


vacuum mvcctable;


select
	relname as tablename,
	n_live_tup as livetuples,
	n_dead_tup as deadtuples
from
	pg_stat_user_tables
where
	relname = 'mvcctable';


select pg_size_pretty(pg_relation_size('mvcctable'));


vacuum full mvcctable;
select * from mvcctable where idcol > 100 and idcol <= 200;