-- This script lists all bands with 'Glam rock' as their main style,
-- ranked by their longevity.
-- The lifespan is calculated using the 'formed' and 'split' years.
-- For bands that are still active, 2022 is used as the current year.
SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
