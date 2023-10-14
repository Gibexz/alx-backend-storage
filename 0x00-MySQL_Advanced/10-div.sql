-- SQL script that creates a function SafeDiv that divides (and returns) the first by the
-- second number or returns 0 if the second number is equal to 0.

delimiter //

drop function if exists SafeDiv;

create function SafeDiv(a int, b int)
returns float
DETERMINISTIC READS SQL DATA
begin
    declare result float default 0;
    if b = 0 then
        return 0;
    else
        set result = a / b;
        return result;
    end if;
end;
//

delimiter ;