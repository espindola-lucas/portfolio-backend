from sqlalchemy import Column, String, Integer
from db import Base, engine

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(70), unique=True)
    email = Column(String(70), unique=True)
    password = Column(String(70))


Base.metadata.create_all(engine)