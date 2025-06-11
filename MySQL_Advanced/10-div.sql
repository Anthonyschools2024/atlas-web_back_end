-- This script creates a function 'SafeDiv' that safely divides two numbers.
-- If the second number (divisor) is 0, the function returns 0.
-- Otherwise, it returns the result of the division.

DELIMITER $$

CREATE FUNCTION SafeDiv (
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;
