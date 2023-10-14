-- SQL script that creates a view need_meeting that lists all students
-- that have a score under 80 (strict) and no last_meeting or more than 1 month.

drop view if exists need_meeting;

create view need_meeting as
SELECT name
from students
where score < 80
and (last_meeting is null or last_meeting <= date_sub(curdate(), interval 1 month));