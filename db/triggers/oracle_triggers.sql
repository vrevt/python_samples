create table orders (id varchar(5), updated_date timestamp);

CREATE OR REPLACE TRIGGER orders_before_update
BEFORE UPDATE
   ON orders
  FOR EACH ROW
DECLARE
   v_username varchar2(10);
BEGIN
      -- Найти персону username, осуществляющего UPDATE в таблице
   SELECT user INTO v_username
   FROM dual;
   -- Обновление поля updated_date до текущей системной даты
   :new.updated_date := sysdate;
   -- Обновление поля updated_by на персону username осуществившую UPDATE
   :new.updated_by := v_username;
END;