import datetime
from flask import jsonify
from daos.bid_dao import BidDAO
from db import Session


class BidStatus:
    @staticmethod
    def update(b_id, status):
        session = Session()
        bid = session.query(BidDAO).filter(BidDAO.id == b_id)[0]
        bid.status.status = status
        bid.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The bid status was updated'}), 200
