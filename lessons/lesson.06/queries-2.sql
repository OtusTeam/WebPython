DROP TABLE users;

CREATE TABLE users (
	id INTEGER NOT NULL,
	username VARCHAR(32) NOT NULL,
	archived BOOLEAN DEFAULT (0),
	created_at DATETIME,
	PRIMARY KEY (id),
	UNIQUE (username)
);
