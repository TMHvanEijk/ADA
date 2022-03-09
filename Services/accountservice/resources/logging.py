import datetime
from flask import jsonify
from daos.account_dao import AccountDAO
from db import Session

class Logging:
    @staticmethod
    def update(a_id):
        session = Session()
        account = session.query(AccountDAO).filter(AccountDAO.id == a_id)[0]
        account.logging.last_login = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The login status was updated'}), 200
