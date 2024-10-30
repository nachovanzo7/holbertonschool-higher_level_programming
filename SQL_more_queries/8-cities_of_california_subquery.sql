-- Listar todas las ciudades de California
SELECT cities.id, cities.name FROM cities, states
WHERE states.name = 'California'
ORDER BY cities.id ASC;