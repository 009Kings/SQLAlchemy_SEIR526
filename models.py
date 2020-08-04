import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table, create_engine
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

  pets = relationship('Pet', back_populates='user', cascade="all, delete, delete-orphan")

  def __repr__(self):
    return f'<User(id={self.id}, name="{self.name}", email="{self.email}", nickname="{self.nickname}")>'

pet_toys = Table(
  'pet_toys', 
  Base.metadata,
  Column('pet_id', ForeignKey('pets.id'), primary_key=True),
  Column('toy_id', ForeignKey('toys.id'), primary_key=True)
)

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
  user = relationship('User', back_populates='pets')
  # user = relationship('User', backref='pets')
  toys = relationship('Toy', secondary=pet_toys, back_populates='pets')

  def __repr__(self):
    return f'<Pet(id={self.id}, name="{self.name}", species="{self.species}", age={self.age}, user_id={self.user_id})>'
  
class Toy(Base):
  __tablename__ = 'toys'

  id = Column(Integer, Sequence('toy_id_seq'), primary_key=True)
  type = Column(String(50), nullable=False, unique=True)
  color = Column(String(50))

  pets = relationship('Pet', secondary=pet_toys, back_populates='toys')

  def __repr__(self):
    return f'<Toy(id={self.id}, type="{self.type}", color="{self.color}")>'

Base.metadata.create_all(engine)