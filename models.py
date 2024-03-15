from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    schedule_id = Column(Integer, ForeignKey("schedule.id"))

class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    week = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    day = Column(String)

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id"))
    name = Column(String)
    lastname = Column(String)

class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id"))
    name = Column(String)

    classroom = relationship("Classroom", backref="subjects")
    students = relationship("Student", backref="subject")
    schedules = relationship("Schedule", backref="subject")

    def __repr__(self):
        return f"<Subject(name={self.name})>"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name