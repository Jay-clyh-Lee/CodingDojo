USE dojos_and_ninjas_schema;
ALTER TABLE dojos AUTO_INCREMENT = 1;
ALTER TABLE ninjas AUTO_INCREMENT = 1;

INSERT INTO dojos (name, created_at, updated_at) VALUES ("Fremont", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Cupertino", NOW(), NOW());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("Sunnyvale", NOW(), NOW());

DELETE FROM dojos WHERE id > 0;

INSERT INTO dojos (name, created_at, updated_at) 
VALUES 
	("Saratoga", NOW(), NOW()),
	("Culver City", NOW(), NOW()),
    ("SF", NOW(), NOW());
    
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	("Mac", "DeKin", 34, NOW(), NOW(), 4),
    ("CK", "Clint", 24, NOW(), NOW(), 4),
    ("AKs", "Ranao", 64, NOW(), NOW(), 4);
    
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	("MacKenze", "Cloud", 34, NOW(), NOW(), 5),
    ("Czent", "Ctrinzae", 24, NOW(), NOW(), 5),
    ("Alpine", "Nanao", 64, NOW(), NOW(), 5);
    
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES
	("Tsa", "Tsing", 34, NOW(), NOW(), 6),
    ("Tom", "Cat", 24, NOW(), NOW(), 6),
    ("Jerry", "Mouse", 64, NOW(), NOW(), 6);
    
SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 5;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojo_id = dojos.id
ORDER BY ninjas.id DESC LIMIT 1;