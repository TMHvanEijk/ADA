from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base

class MessageDAO(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    receiver_id = Column(String)
    sender_id = Column(String)
    context = Column(String)
    send_time = Column(DateTime)
    received_time = Column(DateTime)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("message", uselist=False))

    def __init__(self, receiver_id, sender_id, context, send_time, status):
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.context = context
        self.send_time = send_time
        self.status = status