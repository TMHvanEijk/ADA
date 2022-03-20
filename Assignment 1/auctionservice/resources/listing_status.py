import datetime
from flask import jsonify
from daos.listing_dao import AuctionDAO
from db import Session


class ListingStatus:
    @staticmethod
    def update(a_id, status):
        session = Session()
        auction = session.query(AuctionDAO).filter(AuctionDAO.id == a_id)[0]
        auction.status.status = status
        auction.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The auction status was updated'}), 200
