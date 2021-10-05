USE world;

# preview table
SHOW COLUMNS FROM city;
SHOW COLUMNS FROM country;
SHOW COLUMNS FROM countrylanguage;
SELECT * FROM city
LIMIT 0, 5;
SELECT * FROM country
LIMIT 0, 5;
SELECT * FROM countrylanguage
LIMIT 0, 5;

/*
1. What query would you run to get all the countries that speak Slovene?
 Your query should return the name of the country, language and language percentage.
 Your query should arrange the result by language percentage in descending order. (1)
*/
SELECT name, language, percentage FROM country 
JOIN countrylanguage ON countrylanguage.CountryCode = country.Code
WHERE language = 'Slovene'
ORDER BY percentage DESC;

/*
2. What query would you run to display the total number of cities for each country?
 Your query should return the name of the country and the total number of cities.
 Your query should arrange the result by the number of cities in descending order. (3)
*/
SELECT country.name, COUNT(id) AS cities FROM country
JOIN city ON city.CountryCode = country.Code
GROUP BY country.name
ORDER BY cities DESC;

/*
3. What query would you run to get all the cities in Mexico with a population of greater than 500,000?
 Your query should arrange the result by population in descending order. (1)
*/
SELECT city.name, city.population FROM city
JOIN country ON country.Code = city.CountryCode
WHERE city.population > 500000 AND country.name = 'Mexico'
ORDER BY city.population DESC;

/*
4. What query would you run to get all languages in each country with a percentage greater than 89%?
 Your query should arrange the result by percentage in descending order. (1)
*/
SELECT country.name, language, percentage FROM country
JOIN countrylanguage ON countrylanguage.CountryCode = country.Code
WHERE percentage > 89 
ORDER BY percentage DESC;

/*
5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
*/
SELECT name, surfaceArea, population FROM country
WHERE surfaceArea < 501 AND population > 100000;

/*
6. What query would you run to get countries with only Constitutional Monarchy
 with a capital greater than 200 and a life expectancy greater than 75 years? (1)
*/
SELECT name, governmentForm, capital, lifeExpectancy FROM country
WHERE governmentForm = 'Constitutional Monarchy' AND capital > 200 AND lifeExpectancy > 75;

/*
7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500,000?
 The query should return the Country Name, City Name, District and Population. (2)
*/
SELECT country.name, city.name, district, city.population FROM country
JOIN city ON city.CountryCode = country.Code
WHERE country.name = 'Argentina' AND district = 'Buenos Aires' AND city.population > 500000;

/*
8. What query would you run to summarize the number of countries in each region?
 The query should display the name of the region and the number of countries.
 Also, the query should arrange the result by the number of countries in descending order. (2)
 */
SELECT region, COUNT(name) AS count FROM country
GROUP BY region
ORDER BY count DESC;