-- computes and store the average score for a student.

drop procedure if exists ComputeAverageScoreForUser;
delimiter //
create procedure ComputeAverageScoreForUser(in _id int)
begin
    declare avg_score float;
    select avg(score) into @avg_score
    from corrections
    where user_id = _id;

    update users
    set average_score = @avg_score
    where id = _id;
end;
//

delimiter ;