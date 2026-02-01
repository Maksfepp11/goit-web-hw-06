import sqlite3
from faker import Faker
import random

fake = Faker()
db_name = 'database.db'

def seed_db():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    groups = ['УФФ-24с', 'КН-24', 'ПІ-24']
    for g in groups:
        cur.execute("INSERT INTO groups (name) VALUES (?)", (g,))

    for _ in range(5):
        cur.execute("INSERT INTO teachers (fullname) VALUES (?)", (fake.name(),))

    subjects = ['Вища математика', 'Алгоритми', 'Бази даних', 'Програмування', 'English']
    for s in subjects:
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (s, random.randint(1, 5)))

    for _ in range(50):
        cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?)", (fake.name(), random.randint(1, 3)))

    for s_id in range(1, 51):
        for _ in range(random.randint(10, 20)):
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                        (s_id, random.randint(1, 5), random.randint(60, 100), fake.date_this_year()))

    conn.commit()
    conn.close()
    print("Базу заповнено успішно!")

if __name__ == "__main__":
    seed_db()