from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean

from db import Base


class LoginDAO(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password