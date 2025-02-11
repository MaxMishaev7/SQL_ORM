# import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models_courses_db import create_tables, Course, Homework

DSN = 'postgresql://postgres:hecQWk1974Gmr@localhost:5432/courses'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(autoflush=True, bind=engine)

session = Session()
course = Course()
# courses = [
#   {'name': 'Python'},
#   {'name': 'Java'},
#   {'name': 'C++'},
#   {'name': 'Ruby'},
#   {'name': 'Go'},
# ]

courses = [
  ('Python',),
  ('Java',),
  ('C++',),
  ('Ruby',),
  ('Go',)
]

courses_dicts = [{'name': name} for name in courses]
print(courses_dicts)
session.bulk_insert_mappings(course, courses_dicts)
# course1 = Course(name='Python')
# course2 = Course(name='Java')

homework = Homework()
# homeworks = [
#   {'number': 1, 'description': 'простая домашняя работа', 'course_id': 1},
#   {'number': 2, 'description': 'сложная домашка', 'course_id': 1},
#   {'number': 1, 'description': 'простая домашняя работа', 'course_id': 2}
# ]

homeworks = [
  (1, 'simple homework', 1),
  (2, 'hard homework', 1),
  (1, 'simple homework', 1)
]

homeworks_dicts = [{'number': number, 'description': description, 'course_id': course_id} for number, description, course_id in homeworks]
print(homeworks_dicts, '\n')

session.bulk_insert_mappings(homework, homeworks_dicts)

# session.add_all(course)
# session.commit()
for val in session.query(Course).all():
  print(val)
for v in session.query(Homework).all():
  print(v)
# print(course1)
# print(course2)
session.close()
