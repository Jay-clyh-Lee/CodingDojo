USE friends_schema;

INSERT friends
	(id, first_name, last_name, occupation)
VALUES
	(1, 'Jay', 'Lee', 'Full-Stack Developer'),
    (2, 'Ada', 'Wong', 'Detective'),
    (3, 'Kathie', 'Scout', 'Doctor');
    
SELECT * FROM friends;