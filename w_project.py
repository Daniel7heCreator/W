DATABASE_URL = "postgresql+psycopg2://postgres:nicedogboy228@localhost:5432/test"
import datetime

from sqlalchemy import create_engine, text, select
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine(DATABASE_URL,echo=True)

class Base(DeclarativeBase):
    pass

class Lesson(Base):
    __tablename__ = "lessons"
    id: Mapped[int] = mapped_column(primary_key=True)
    number_lesson: Mapped[int] = mapped_column()
    theme_lesson: Mapped[str] = mapped_column(String(50))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

class Course(Base):
    __tablename__ = "courses"   
    id: Mapped[int] = mapped_column(primary_key=True)
    name_course: Mapped[str] = mapped_column(String(50))
    price_course: Mapped[int] = mapped_column()

class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(50))

class CourseTeacher(Base):
    __tablename__ = "course_teachers"
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(50))

class Homework(Base):
    __tablename__ = "homeworks"
    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int] = mapped_column()
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))

class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    price: Mapped[int] = mapped_column()
    enrolled_at: Mapped(datetime.date) = mapped_column()