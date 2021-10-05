USE dojos_and_ninjas_schema;

# insert 3
INSERT INTO dojos
	(id, name, created_at, updated_at) 
VALUES
	(1, 'Coding Dojo San Jose', NOW(), NOW()),
    (2, 'Coding Dojo Mountain View', NOW(), NOW()),
    (3, 'Coding Dojo Los Angeles', NOW(), NOW());

# delete all
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

# creat 3 dojos
INSERT INTO dojos
	(id, name, created_at, updated_at)
VALUES
	(1, 'Coding Dojo San Jose', NOW(), NOW()),
    (2, 'Coding Dojo Mountain View', NOW(), NOW()),
    (3, 'Coding Dojo Los Angeles', NOW(), NOW());

# add 3 ninjas to 1st dojo
INSERT INTO ninjas
	(id, first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	(1, 'John', 'Smith', 30, NOW(), NOW(), 1),
    (2, 'Jason', 'McGregor', 30, NOW(), NOW(), 1),
    (3, 'Jr. Ken', 'Lawson', 30, NOW(), NOW(), 1);

# add 3 ninjas to 2nd dojo
INSERT INTO ninjas
	(id, first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	(4, 'Michael', 'Smith', 20, NOW(), NOW(), 2),
    (5, 'Mika', 'Ting', 20, NOW(), NOW(), 2),
    (6, 'Kaden', 'Loung', 20, NOW(), NOW(), 2);

# add 3 ninjas to 3rd dojo
INSERT INTO ninjas
	(id, first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	(7, 'Ross', 'Smith', 20, NOW(), NOW(), 3),
    (8, 'Rosy', 'Ting', 20, NOW(), NOW(), 3),
    (9, 'Cathie', 'Loung', 20, NOW(), NOW(), 3);
    
# retrieve all the ninjas from the 1st dojo
SELECT * FROM ninjas
WHERE dojo_id = 1;

# retrieve all the ninjas from the 2nd dojo
SELECT * FROM ninjas
WHERE dojo_id = 2;

# retrieve all the ninjas from the 3rd dojo
SELECT * FROM ninjas
WHERE dojo_id = 3;
