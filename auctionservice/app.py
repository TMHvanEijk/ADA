from flask import Flask, request

from db import Base, engine
from resources.listing import Listing
from resources.listing_status import ListingStatus
from resources.bid import Bid
from resources.bid_status import BidStatus

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/auctions', methods=['POST'])
def create_auction():
    req_data = request.get_json()
    return Auction.create(req_data)


@app.route('/auctions/<a_id>', methods=['GET'])
def get_auction(a_id):
    return Auction.get(a_id)


@app.route('/auctions/<a_id>/status', methods=['PUT'])
def update_auction_status(a_id):
    status = request.args.get('status')
    return Status.update(a_id, status)


@app.route('/auctions/<a_id>', methods=['DELETE'])
def delete_auction(a_id):
    return Auction.delete(a_id)


@app.route('/bids', methods=['POST'])
def create_bid():
    req_data = request.get_json()
    return Bid.create(req_data)


@app.route('/bids/<b_id>', methods=['GET'])
def get_bid(b_id):
    return Bid.get(b_id)


@app.route('/bids/<b_id>/status', methods=['PUT'])
def update_bid_status(b_id):
    status = request.args.get('status')
    return Status.update(b_id, status)


@app.route('/bids/<b_id>', methods=['DELETE'])
def delete_bid(b_id):
    return Bid.delete(b_id)


app.run(host='0.0.0.0', port=5000)
