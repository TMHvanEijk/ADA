from flask import jsonify
from daos.account_dao import AccountDAO
from db import Session
from daos.login_dao import LoginDAO

class Login:
    @staticmethod
    def update(email, old_password, new_password):
        session = Session()
        account = session.query(AccountDAO).filter((AccountDAO.customer_email == email) & (AccountDAO.customer_password == old_password))[0]
        combination = session.query(LoginDAO).filter((LoginDAO.email == email) & (LoginDAO.password == old_password))[0]

        account.customer_password = new_password
        combination.password = new_password

        session.commit()

        return jsonify({"message" : "The password has been changed."}), 200

    @staticmethod
    def get_password(a_id, email):
        session = Session()
        combination = session.query(LoginDAO).filter(LoginDAO.email == email)[0]

        if combination:
            text_out = {
                "password:":combination.password
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({"message":"This combination of email and password does not exist"}), 404

    @staticmethod
    def get_email(a_id, password):
        session = Session()
        combination = session.query(LoginDAO).filter(LoginDAO.password == password)[0]

        if combination:
            text_out = {
                "email:":combination.email
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({"message":"This combination of email and password does not exist"}), 404