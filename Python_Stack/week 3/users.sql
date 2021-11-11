SET SQL_SAFE_UPDATES = 0;

USE users_schema;

ALTER TABLE users AUTO_INCREMENT = 1;

# Query: Create 3 new users
INSERT INTO users (first_name, last_name, email)
VALUES 
	("Michael", "Archangel", "MichaelArchangel@heaven.com"),
    ("Gabriel", "Archangel", "GabrielArchangel@heaven.com"),
    ("Ariel", "Archangel", "ArielArchangel@heaven.com");
 
 # Query: Retrieve all the users
 SELECT * FROM users;
 
 # Query: Retrieve the first user using their email address
 SELECT * FROM users WHERE email = "MichaelArchangel@heaven.com";
 
 # Query: Retrieve the last user using their id
 SELECT * FROM users ORDER BY id DESC LIMIT 1;
 
 # Query: Change the user with id=3 so their last name is Pancakes
 UPDATE users SET last_name = "Pancakes" WHERE id = 3;
 
 # Query: Delete the user with id=2 from the database
 DELETE FROM users WHERE id = 2;
 
# Query: Get all the users, sorted by their first name
SELECT * FROM users ORDER BY first_name;

# BONUS Query: Get all the users, sorted by their first name in descending order
SELECT * FROM users ORDER BY first_name DESC;
