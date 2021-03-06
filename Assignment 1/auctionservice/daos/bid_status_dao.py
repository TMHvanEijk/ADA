from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class BidStatusDAO(Base):
    __tablename__ = 'bidstatus'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, status, last_update):
        self.status = status
        self.last_update = last_update
