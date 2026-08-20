CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, status VARCHAR(255)NOT NULL DEFAULT 'pending');

INSERT INTO tasks (title,status) VALUES ('Learn Docker','completed'),('Test production API','pending');
