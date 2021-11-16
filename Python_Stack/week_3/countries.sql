/*
1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)

2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)

3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)

5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)

6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)

7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500,000? The query should return the Country Name, City Name, District and Population. (2)

8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
*/

# ANSWERS:

#1.
SELECT name, language, percentage FROM countries
LEFT JOIN languages ON countries.id = country_id
WHERE language = "Slovene"
ORDER BY percentage DESC;

#2.
SELECT countries.name, COUNT(cities.name) AS c FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY c DESC;

#3.
SELECT cities.name, cities.population AS p, country_id FROM countries
LEFT JOIN cities ON countries.id = country_id
WHERE cities.population > 500000 AND countries.name = "Mexico"
ORDER BY p DESC;

#4.
SELECT name, language, percentage FROM countries
LEFT JOIN languages ON countries.id = country_id
WHERE percentage > 89
ORDER BY percentage DESC;

#5.
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;

#6.
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;

#7.
SELECT countries.name, cities.name, district, cities.population FROM countries
LEFT JOIN cities ON countries.id = country_id
WHERE countries.name = "Argentina" AND district = "Buenos Aires" AND cities.population > 500000;

#8.
SELECT region, COUNT(*) AS c FROM countries
GROUP BY region
ORDER BY c DESC;
