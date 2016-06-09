import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    #creating the categories table
    __tablename__ = 'category'

    name = Column(String(200),nullable = False)
    id = Column(Integer, primary_key = True)

class CategoryItem(Base):
    #creating the items table
    __tablename__ = 'category_item'

    title = Column(String(80),nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(1024))
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship(Category)

    #We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

       return {
           'title'         : self.title,
           'description'   : self.description,
           'id'            : self.id
           }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)