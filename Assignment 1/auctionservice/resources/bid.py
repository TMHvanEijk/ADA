from datetime import datetime

from flask import jsonify

from constant import STATUS_CREATED
from daos.bid_dao import BidDAO
from daos.bid_status_dao import BidStatusDAO
from db import Session


class Bid:
    @staticmethod
    def create(body):
        session = Session()
        bid = BidDAO(body['buyer_id'], body['bid_amount'], body['auction'],
                               BidStatusDAO(STATUS_CREATED, datetime.now()))
        session.add(bid)
        session.commit()
        session.refresh(bid)
        session.close()
        return jsonify({'bid_id': bid.id}), 200

    @staticmethod
    def get(b_id):
        session = Session()
        bid = session.query(BidDAO).filter(BidDAO.id == b_id).first()

        if bid:
            status_obj = bid.status
            text_out = {
                "buyer_id:": bid.buyer_id,
                "bid_amount": bid.bid_amount,
                "auction": bid.auction,
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no bid with id {d_id}'}), 404

    @staticmethod
    def delete(b_id):
        session = Session()
        effected_rows = session.query(BidDAO).filter(BidDAO.id == b_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no bid with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The bid was removed'}), 200
