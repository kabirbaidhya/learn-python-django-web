
CREATE TABLE users (
    id serial PRIMARY KEY,
    first_name varchar (20) NOT NULL,
    last_name varchar (20) NOT NULL,
    email varchar (50) NOT NULL UNIQUE,
    address varchar (100),
    password varchar (50) NOT NULL,
    created_at timestamp NOT NULL
);

CREATE TABLE todos (
    id serial PRIMARY KEY,
    user_id integer NOT NULL REFERENCES users(id),
    title varchar (50) NOT NULL,
    description text,
    completed boolean NOT NULL DEFAULT false,
    created_at timestamp NOT NULL
);

-- This is a comment.
-- Insert Users
INSERT INTO users (first_name, last_name, email, address, password, created_at)
VALUES
('Test 1', 'Test', 'test1@test.com', 'Kathmandu, Nepal', 'test', NOW()),
('Test 2', 'Test', 'test2@test.com', 'Kathmandu, Nepal', 'test', NOW()),
('Test 3', 'Test', 'test3@test.com', 'Kathmandu, Nepal', 'test', NOW());


INSERT INTO todos (user_id, title, created_at)
VALUES
(1, 'Test to do 1', NOW()),
(1, 'Test to do 2', NOW()),
(2, 'Test to do 3', NOW()),
(2, 'Test to do 4', NOW()),
(2, 'Test to do 5', NOW()),
(3, 'Test to do 6', NOW()),
(3, 'Test to do 7', NOW()),
(3, 'Test to do 8', NOW()),
(1, 'Test to do 9', NOW()),
(1, 'Test to do 10', NOW()),
(2, 'Test to do 11', NOW()),
(2, 'Test to do 12', NOW()),
(1, 'Test to do 13', NOW()),
(1, 'Test to do 14', NOW()),
(3, 'Test to do 15', NOW()),
(3, 'Test to do 16', NOW());

--
-- Select Query
SELECT  t.id, title, user_id, t.created_at,
        concat(u.first_name, ' ', u.last_name) as user_full_name
from todos as t
JOIN users as u ON u.id = t.user_id;
