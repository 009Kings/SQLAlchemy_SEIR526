import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine

# db uri = dbEngine://username:password@netloc:port/dbname
engine = create_engine('postgresql://localhost/sqlalchemy_test1', echo=True)

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True)
  nickname = Column(String(50))

  def __repr__(self):
    return f'<User(id={self.id}, name="{self.name}", email="{self.email}", nickname="{self.nickname}")>'

Base.metadata.create_all(engine)