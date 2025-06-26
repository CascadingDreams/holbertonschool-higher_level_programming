-- lists all cities contained in the database in ascen order by cities.id
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;