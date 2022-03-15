from flask import Flask, request

from db import Base, engine
from resources.message import Message
from resources.status import Status

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)

@app.route('/messages', methods=['POST'])
def create_message():
    req_data = request.get_json()
    return Message.create(req_data)

@app.route('/messages/<d_id>', methods=['GET'])
def get_message(d_id):
    return Message.get(d_id)


@app.route('/messages/<d_id>/status', methods=['PUT'])
def update_message_status(d_id):
    status = request.args.get('status')
    return Status.update(d_id, status)


@app.route('/messages/<d_id>', methods=['DELETE'])
def delete_message(d_id):
    return Message.delete(d_id)


app.run(host='0.0.0.0', port=5000)