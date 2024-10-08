import random
from faker import Faker
from connection import get_connection

fake = Faker()

NUM_GROUPS = 3
NUM_TEACHERS = 5
NUM_STUDENTS = 30
NUM_SUBJECTS = 5
MAX_GRADES_PER_STUDENT = 20

def insert_data():
    with get_connection() as conn:
        if conn is None:
            print('Failed to connect to the database')
            return

        group_ids = []
        for i in range(NUM_GROUPS):
            group_name = f'Group {i + 1}'
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO groups (id, name) VALUES (%s, %s)",
                    (i + 1, group_name)
                )
                group_ids.append(i + 1)

        teacher_ids = []
        for i in range(NUM_TEACHERS):
            teacher_name = fake.name()
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO teachers (id, name) VALUES (%s, %s)",
                    (i + 1, teacher_name)
                )
                teacher_ids.append(i + 1)

        student_ids = []
        for i in range(NUM_STUDENTS):
            student_name = fake.name()
            group_id = random.choice(group_ids)
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (id, name, group_id) VALUES (%s, %s, %s)",
                    (i + 1, student_name, group_id)
                )
                student_ids.append(i + 1)

        subject_ids = []
        for i in range(NUM_SUBJECTS):
            subject_name = fake.bs()  # Generate a random subject name using Faker
            teacher_id = random.choice(teacher_ids)
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO subjects (id, name, teacher_id) VALUES (%s, %s, %s)",
                    (i + 1, subject_name, teacher_id)
                )
                subject_ids.append(i + 1)

        for student_id in student_ids:
            for _ in range(random.randint(1, MAX_GRADES_PER_STUDENT)):
                subject_id = random.choice(subject_ids)
                grade = random.randint(1, 12)  # Random grade between 1 and 12
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)",
                        (student_id, subject_id, grade)
                    )

        print("Data inserted successfully!")

