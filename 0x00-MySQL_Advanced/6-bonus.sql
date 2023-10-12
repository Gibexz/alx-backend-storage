-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student

delimiter //

create procedure AddBonus (in user_id int, in project_name varchar(255), in score int)
begin
    declare project_id int;

    -- Checks if the project already exists, if not, create it
    select id into project_id
    from projects
    where name = project_name;
    
    if project_id is null then
        insert into projects (name) values (project_name);
        set project_id = last_insert_id();
    end if;

    -- add the correction
    insert into corrections (user_id, project_id, score) values (user_id, project_id, score);
end;

//
delimiter ;