-- This script creates a trigger that decreases the quantity of an item
-- after a new order is created.
-- The quantity in the 'items' table is reduced by the amount in the new order.

DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
