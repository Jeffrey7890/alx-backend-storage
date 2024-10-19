--  list all bands with glam rock
SELECT band_name, (2022-formed) AS lifespan FROM metal_bands WHERE INSTR(style, 'Glam rock') > 0 ORDER BY lifespan DESC;
