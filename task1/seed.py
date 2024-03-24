from faker import Faker
import sqlite3
import random

fake = Faker()

# Підключення до бази даних
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# # Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))
    conn.commit()

# Заповнення таблиці status
status_names = ['new', 'in progress', 'completed']
for name in status_names:
    cursor.execute("INSERT INTO status (name) VALUES (?)", (name,))
    conn.commit()

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.text(max_nb_chars=50)
    description = fake.text()
    status_id = random.randint(1, len(status_names))
    user_id = random.randint(1, 10)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", (title, description, status_id, user_id))
    conn.commit()

# Закриваємо з'єднання з базою даних
conn.close()
