from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    base_experience = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
