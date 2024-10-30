-- Listar todas las ciudades de California
SELECT cities.id, cities.name FROM cities, states
WHERE states.name = 'California' and state_id = states.id
ORDER BY cities.id ASC;