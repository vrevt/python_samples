CREATE OR REPLACE FUNCTION public.test()
 RETURNS SETOF integer
 LANGUAGE plpgsql
AS $function$
declare
    i int4;
begin
    for i in 1..3 loop
        return next i;
        perform pg_sleep(1);
    end loop;
    return;
end;
$function$;

select test()