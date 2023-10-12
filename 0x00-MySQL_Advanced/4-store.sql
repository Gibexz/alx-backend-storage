-- SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.

delimiter //
create trigger update_item_quantity after insert on orders
for each row
begin
    update items
    set quantity = quantity - new.number 
    where name = new.item_name;
end;
//
delimiter ;