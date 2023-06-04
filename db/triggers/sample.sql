delimeter //
create trigger sample
    before
        update on some_table
    for each row
    begin
        set other_table.col = other_table.col * 1.1;
    end //
delimeter;


DELIMITER //
CREATE TRIGGER After_Delete_salespeople
AFTER DELETE
ON salespeople
FOR EACH ROW
BEGIN
    DELETE FROM orders
    WHERE orders.snum = OLD.snum;
END //
DELIMITER ;