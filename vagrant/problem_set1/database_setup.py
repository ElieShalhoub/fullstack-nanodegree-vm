import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    #creating the shelter table
    __tablename__ = 'shelter'

    name = Column(String(80),nullable = False)
    address = Column(String(80))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(String(80))
    website = Column(String(80))
    id = Column(Integer, primary_key = True)

class Puppy(Base):
    #creating the puppy  table
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key = True)
    name = Column(String(80),nullable = False)
    dob = Column(String(10))
    gender = Column(String(1))
    weight = Column(Integer)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))

    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
