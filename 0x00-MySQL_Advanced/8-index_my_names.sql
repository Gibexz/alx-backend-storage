-- SQL script that creates an index idx_name_first on
-- the table names and the first letter of name

create INDEX idx_name_first on names (name(1));