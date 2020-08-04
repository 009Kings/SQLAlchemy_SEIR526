import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, create_engine
from sqlalchemy.orm import relationship

# db uri = dbEngine://username:password@netloc:port/dbname
engine = create_engine('postgresql://localhost/sqlalchemy_test1', echo=True)

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True)
  nickname = Column(String(50))

  # pets = relationship('Pet', back_populates='user')

  def __repr__(self):
    return f'<User(id={self.id}, name="{self.name}", email="{self.email}", nickname="{self.nickname}")>'

# Create a Pet
class Pet(Base):
  __tablename__ = 'pets'

  # SQL Table stuff
  id = Column(Integer, Sequence('pet_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  species = Column(String, nullable=False)
  age = Column(Integer)
  user_id = Column(ForeignKey('users.id'))

  # Model functionality
  # user = relationship('User', back_populates='pets')
  user = relationship('User', backref='pets')

  def __repr__(self):
    return f'<Pet(id={self.id}, name="{self.name}", species="{self.species}", age={self.age}, user_id={self.user_id})>'

Base.metadata.create_all(engine)