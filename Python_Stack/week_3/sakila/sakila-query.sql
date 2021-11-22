USE sakila;
SET SQL_SAFE_UPDATES = 0;

# 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city, country.country FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id
WHERE address.city_id = 312;


# 2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, title, description, release_year, rating, special_features, category.name AS genre FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = "Comedy"
ORDER BY title;


# 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
SELECT actor.actor_id, first_name, last_name, title, description, release_year FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5;


# 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.
SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city, store.store_id FROM customer
LEFT JOIN address ON customer.address_id = address.address_id
LEFT JOIN store ON store.address_id = address.address_id
LEFT JOIN city ON city.city_id = address.city_id
WHERE store.store_id = 1 AND city.city_id IN (1, 42, 312, 459);


#5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT title, description, release_year, rating, special_features FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE rating = "G" AND special_features LIKE "%behind the scenes%";


#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.
SELECT film.film_id, title, actor.actor_id, CONCAT(CONCAT(SUBSTRING(actor.first_name, 1,1), LOWER(SUBSTRING(actor.first_name, 2, 100))), " ", CONCAT(SUBSTRING(actor.last_name, 1,1), LOWER(SUBSTRING(actor.last_name, 2, 100)))) AS full_name FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;


#7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT title, description, release_year, rating, special_features, category.name AS genre FROM film
LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id
LEFT JOIN inventory ON inventory.film_id = film.film_id
LEFT JOIN rental ON rental.inventory_id = inventory.inventory_id
LEFT JOIN payment ON payment.rental_id = rental.rental_id
WHERE amount = 2.99 AND category.name = "Drama";


-- SELECT DISTINCT TABLE_NAME 
--     FROM INFORMATION_SCHEMA.COLUMNS
--     WHERE COLUMN_NAME IN ('film_id','rental_id')
--         AND TABLE_SCHEMA='sakila';


#8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT title, description, release_year, rating, special_features, category.name AS genre, CONCAT(CONCAT(SUBSTRING(actor.first_name, 1,1), LOWER(SUBSTRING(actor.first_name, 2, 100))), " ", CONCAT(SUBSTRING(actor.last_name, 1,1), LOWER(SUBSTRING(actor.last_name, 2, 100)))) AS full_name FROM film
LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id
LEFT JOIN film_actor ON film_actor.film_id = film.film_id
LEFT JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE CONCAT(actor.first_name, " ", actor.last_name) = "SANDRA KILMER" AND category.name = "Action";

