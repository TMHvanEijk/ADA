from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base

class LoggingDAO(Base):
    __tablename__ = "logging"

    id = Column(Integer, primary_key=True)
    last_login = Column(TIMESTAMP(timezone=False))

    def __init__(self, last_login):
        self.last_login = last_login