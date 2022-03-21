from sqlalchemy import Column, String, Integer, TIMESTAMP

from db import Base


class AuctionStatusDAO(Base):
    __tablename__ = 'auctionstatus'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    status = Column(String)
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, status, last_update):
        self.status = status
        self.last_update = last_update
