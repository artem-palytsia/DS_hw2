-- 1
SELECT title, user_id FROM tasks 

-- 2
SELECT title FROM tasks 
WHERE status_id  = 1

-- 3
UPDATE tasks SET status_id = 2 WHERE user_id = 3

-- 4
SELECT id, fullname, email
FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New task', 'Description of the new task', 1, 1)

-- 6 
SELECT title FROM tasks
WHERE status_id IS NOT 3

-- 7 
DELETE FROM tasks WHERE id = 5

-- 8
SELECT fullname, email
FROM users
WHERE email LIKE 'kenneth09@example.org'

-- 9
UPDATE users SET fullname = 'TEST'
WHERE id = 1

-- 10
SELECT COUNT(status_id) as task_count, status_id  
FROM tasks
GROUP BY status_id 

-- 11
SELECT tasks.id, tasks.title, users.fullname, users.email
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE email LIKE '%@example.net'

-- 12
SELECT id, title
FROM tasks
WHERE description = ''

-- 13
SELECT users.id, users.fullname tasks.status_id AS In_Progress
FROM users
JOIN tasks ON users.id = tasks.user_id
WHERE status_id = 2

-- 14
SELECT users.id, users.fullname, COUNT(tasks.id) AS tasks_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname;
