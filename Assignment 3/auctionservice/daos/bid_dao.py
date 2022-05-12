from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship, backref

from daos.bid_status_dao import BidStatusDAO
from daos.listing_dao import AuctionDAO
from db import Base


class BidDAO(Base):
    __tablename__ = 'bid'
    id = Column(Integer, primary_key=True)
    buyer_id = Column(String)
    bid_amount = Column(Float)
    auction_id = Column(Integer)

    status_id = Column(Integer, ForeignKey('bidstatus.id'))
    status = relationship(BidStatusDAO.__name__, backref=backref("bid", uselist=False))

    def __init__(self, buyer_id, bid_amount, auction_id, status):
        self.buyer_id = buyer_id
        self.bid_amount = bid_amount
        self.auction_id = auction_id
        self.status = status
