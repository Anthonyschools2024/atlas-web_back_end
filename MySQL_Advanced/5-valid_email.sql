-- This script creates a trigger that resets the 'valid_email' attribute
-- only when the 'email' for a user has been changed.
-- This ensures that a user must re-validate their email after an update.

DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
