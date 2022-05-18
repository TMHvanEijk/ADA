from datetime import datetime

from flask import jsonify

from constant import STATUS_SALE
from daos.listing_dao import AuctionDAO
from daos.listing_status_dao import AuctionStatusDAO
from db import Session


class Listing:
    @staticmethod
    def create(body):
        session = Session()
        auction = AuctionDAO(body['seller_id'], body['category_id'], body['starting_price'],
                               AuctionStatusDAO(STATUS_SALE, datetime.now()))
        session.add(auction)
        session.commit()
        session.refresh(auction)
        session.close()
        return jsonify({'auction_id': auction.id}), 200

    @staticmethod
    def get(a_id):
        session = Session()
        auction = session.query(AuctionDAO).filter(AuctionDAO.id == a_id).first()

        if auction:
            status_obj = auction.status
            text_out = {
                "seller_id": auction.seller_id,
                "category_id": auction.category_id,
                "starting_price": auction.starting_price,
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no auction with id {d_id}'}), 404

    @staticmethod
    def delete(a_id):
        session = Session()
        effected_rows = session.query(AuctionDAO).filter(AuctionDAO.id == a_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no auction with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The auction was removed'}), 200
