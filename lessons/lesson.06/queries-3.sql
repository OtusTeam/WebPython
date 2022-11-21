DROP TABLE users;

CREATE TABLE users
(
    id         SERIAL      NOT NULL,
    username   VARCHAR(32) NOT NULL,
    archived   BOOLEAN                     DEFAULT false,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
    PRIMARY KEY (id),
    UNIQUE (username)
);


INSERT INTO users (username, archived)
VALUES ('john', FALSE)
RETURNING users.id;

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 1;

INSERT INTO users (username, archived)
VALUES
    ('bob', FALSE),
    ('alice', FALSE),
    ('kate', FALSE),
    ('nick', FALSE);

