import datetime
from flask import jsonify
from daos.message_dao import MessageDAO
from db import Session


class Status:
    @staticmethod
    def update(d_id, status):
        session = Session()
        message = session.query(MessageDAO).filter(MessageDAO.id == d_id)[0]
        message.status.status = status
        message.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The message status was updated'}), 200
