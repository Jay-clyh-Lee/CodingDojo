USE friendships;

SET SQL_SAFE_UPDATES = 0;

INSERT INTO users (first_name, last_name)
VALUES 
	("John", "the 3rd"),
    ("Katie", "Star"),
    ("Don", "Carleone"),
    ("Cratin", "Gremlin"),
    ("Random", "Name"),
    ("Tom", "the Stardenburdenhardenbart");
    
INSERT INTO friendships (user_id, friend_id)
VALUES
	(2,1), (2,3), (2,5), (3,2), (3,5), (4,3), (5,1), (5,6), (6,2), (6,3);

SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
JOIN friendships ON user_id = users.id
LEFT JOIN users AS friends ON friends.id = friend_id
ORDER BY users.first_name ASC;

# test query
SELECT * FROM users LEFT JOIN friendships ON friend_id = users.id WHERE users.id = 1;

# NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
LEFT JOIN friendships ON friend_id = users.id
LEFT JOIN users AS friends ON friends.id = user_id
WHERE users.first_name = "John";

# NINJA Query: Return the count of all friendships
SELECT COUNT(*) FROM friendships;

# NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT first_name, last_name, COUNT(*) AS c FROM users
LEFT JOIN friendships ON friend_id = users.id
GROUP BY first_name
ORDER BY c DESC LIMIT 1;

# NINJA Query: Return the friends of the third user in alphabetical order
SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
LEFT JOIN friendships ON friend_id = users.id
LEFT JOIN users AS friends ON friends.id = user_id
WHERE users.id = 3
ORDER BY friends.first_name ASC;
