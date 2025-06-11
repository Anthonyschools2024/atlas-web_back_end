-- This script creates a composite index named 'idx_name_first_score'.
-- The index covers the first letter of the 'name' column and the 'score' column
-- to optimize queries that filter on both attributes.

CREATE INDEX idx_name_first_score ON names (name(1), score);
