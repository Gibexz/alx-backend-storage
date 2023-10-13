-- computes and store the average score for a student.

delimiter //

create procedure ComputeAverageScoreForUser(in user_id int)
begin
    declare avg_score float;
    select avg(score) into @avg_score
    from corrections
    where user_id = user_id;
    update users set average_score = @avg_score where id = user_id;
end;
//

delimiter ;