from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import AuctionStatusDAO
from db import Base


class AuctionDAO(Base):
    __tablename__ = 'auction'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    seller_id = Column(String)
    category_id = Column(String)
    starting_price = Column(Float)

    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship(AuctionStatusDAO.__name__, backref=backref("auction", uselist=False))

    def __init__(self, seller_id, category_id, starting_price, status):
        self.seller_id = seller_id
        self.category_id = category_id
        self.starting_price = starting_price
        self.status = status



