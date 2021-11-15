-- first
-- CREATE TABLE users (
-- 	id INTEGER NOT NULL,
-- 	username VARCHAR NOT NULL,
-- 	PRIMARY KEY (id),
-- 	UNIQUE (username)
-- );


-- third

-- CREATE TABLE users (
-- 	id INTEGER NOT NULL,
-- 	username VARCHAR NOT NULL,
-- 	is_staff BOOLEAN NOT NULL,
-- 	PRIMARY KEY (id),
-- 	UNIQUE (username)
-- );

-- orm examples

-- 1.
CREATE TABLE users (
	id INTEGER NOT NULL,
	username VARCHAR NOT NULL,
	is_staff BOOLEAN NOT NULL,
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (username)
);

-- select

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users;

-- by id
SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 1;

-- by usernames
SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
WHERE users.username IN ('sam', 'john');

-- create posts table

CREATE TABLE posts (
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
	id INTEGER NOT NULL,
	title VARCHAR DEFAULT '' NOT NULL,
	author_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(author_id) REFERENCES users (id)
);

-- create posts

INSERT INTO posts (title, author_id) VALUES ('Flask lesson', 3);
INSERT INTO posts (title, author_id) VALUES ('Django lesson', 2);

-- get posts with authors

SELECT posts.created_at   AS posts_created_at,
       posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.author_id    AS posts_author_id,
       users_1.created_at AS users_1_created_at,
       users_1.id         AS users_1_id,
       users_1.username   AS users_1_username,
       users_1.is_staff   AS users_1_is_staff
FROM posts
 LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.author_id;


-- get users with posts
SELECT users.created_at   AS users_created_at,
       users.id           AS users_id,
       users.username     AS users_username,
       users.is_staff     AS users_is_staff,
       posts_1.created_at AS posts_1_created_at,
       posts_1.id         AS posts_1_id,
       posts_1.title      AS posts_1_title,
       posts_1.author_id  AS posts_1_author_id
FROM users
     LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.author_id;

-- query lessons
SELECT posts.created_at   AS posts_created_at,
       posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.author_id    AS posts_author_id,
       users_1.created_at AS users_1_created_at,
       users_1.id         AS users_1_id,
       users_1.username   AS users_1_username,
       users_1.is_staff   AS users_1_is_staff
FROM posts
         LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.author_id
WHERE lower(posts.title) LIKE lower('%lesson%');

-- get all lessons authors
SELECT users.created_at AS users_created_at,
       users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff
FROM users
     JOIN posts ON users.id = posts.author_id
WHERE lower(posts.title) LIKE lower('%lesson%');



-- create tags table
CREATE TABLE tags (
	id INTEGER NOT NULL,
	name VARCHAR NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (name)
);

-- create posts_tags_association_table
CREATE TABLE posts_tags_association_table (
	post_id INTEGER NOT NULL,
	tag_id INTEGER NOT NULL,
	PRIMARY KEY (post_id, tag_id),
	FOREIGN KEY(post_id) REFERENCES posts (id),
	FOREIGN KEY(tag_id) REFERENCES tags (id)
);


-- show_posts_with_tags_and_authors
SELECT posts.created_at   AS posts_created_at,
       posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.author_id    AS posts_author_id,
       users_1.created_at AS users_1_created_at,
       users_1.id         AS users_1_id,
       users_1.username   AS users_1_username,
       users_1.is_staff   AS users_1_is_staff,
       tags_1.id          AS tags_1_id,
       tags_1.name        AS tags_1_name
FROM posts
 LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.author_id
 LEFT OUTER JOIN (
     posts_tags_association_table AS posts_tags_association_table_1
         JOIN tags AS tags_1
         ON tags_1.id = posts_tags_association_table_1.tag_id)
             ON posts.id = posts_tags_association_table_1.post_id;

-- find_users_by_tags
SELECT users.created_at AS users_created_at,
       users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff
FROM users
     JOIN posts ON users.id = posts.author_id
     JOIN posts_tags_association_table AS posts_tags_association_table_1
          ON posts.id = posts_tags_association_table_1.post_id
     JOIN tags ON tags.id = posts_tags_association_table_1.tag_id
WHERE tags.name = 'news';

