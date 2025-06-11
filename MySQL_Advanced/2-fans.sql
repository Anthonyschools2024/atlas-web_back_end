-- This script ranks the origins of metal bands by their total number of non-unique fans.
-- The output displays the origin and the total fan count, ordered from highest to lowest.
SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
