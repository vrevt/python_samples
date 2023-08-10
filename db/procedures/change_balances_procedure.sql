create table stored_Procedure_Prac (
    id int generated by default as identity,
    name varchar(100) not null,
    balance dec(15, 2) not null,
    primary key(id)
);

insert into stored_Procedure_Prac(name, balance)
values('Don', 400000);

insert into stored_Procedure_Prac(name, balance)
values('Bob', 400000);


select * from stored_Procedure_Prac;


create or replace procedure prac_transfer(
   sender int,
   receiver int,
   amount dec
)
language plpgsql
as $$
begin
    -- subtracting the amount from the sender's account
    update stored_Procedure_Prac
    set balance = balance - amount
    where id = sender;

    -- adding the amount to the receiver's account
    update stored_Procedure_Prac
    set balance = balance + amount
    where id = receiver;

    commit;
end;$$;


call prac_transfer(1, 2, 1000);

select * from stored_Procedure_Prac;