from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table (no mapped class needed)
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("student.id"), primary_key=True),
    Column("course_id", ForeignKey("course.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    # Many-to-many
    courses: Mapped[list["Course"]] = relationship(
        secondary=student_course, back_populates="students"
    )

class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

    students: Mapped[list["Student"]] = relationship(
        secondary=student_course, back_populates="courses"
    )
