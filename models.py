from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique = True)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"