-- This script creates a view named 'need_meeting'.
-- The view lists all students who have a score strictly under 80
-- and have either never had a meeting or had their last meeting over a month ago.

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE
    score < 80 AND
    (
        last_meeting IS NULL
        OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    );
