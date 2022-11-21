CREATE TABLE authors (
	id INTEGER NOT NULL,
	username VARCHAR(32) NOT NULL,
	email VARCHAR(200),
	bio TEXT,
	PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);


