from datetime import datetime

from flask import jsonify

from constant import STATUS_SEND
from daos.message_dao import MessageDAO
from daos.status_dao import StatusDAO
from db import Session


class Message:
    @staticmethod
    def create(body):
        session = Session()
        message = MessageDAO(body['receiver_id'], body['sender_id'], body['context'],
                               datetime.strptime(body['send_time'], '%Y-%m-%d %H:%M:%S.%f'),
                               StatusDAO(STATUS_SEND, datetime.now()))
        session.add(message)
        session.commit()
        session.refresh(message)
        session.close()
        return jsonify({'message_id': message.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
        message = session.query(MessageDAO).filter(MessageDAO.id == d_id).first()

        if message:
            status_obj = message.status
            text_out = {
                "receiver_id:": message.receiver_id,
                "sender_id": message.sender_id,
                "context": message.context,
                "send_time": message.send_time.isoformat(),
                "status": {
                    "status": status_obj.status,
                    "last_update": status_obj.last_update.isoformat(),
                }
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no message with id {d_id}'}), 404

    @staticmethod
    def delete(d_id):
        session = Session()
        effected_rows = session.query(MessageDAO).filter(MessageDAO.id == d_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no message with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The message was removed'}), 200
