from datetime import datetime

from flask import jsonify

from daos.account_dao import AccountDAO
from daos.settings_dao import SettingsDAO
from db import Session

class Account:
    @staticmethod
    def create(body):
        session = Session()
        account = AccountDAO(body['customer_email'], body['customer_password'], body['customer_name'], body['customer_address'],
                             body['customer_birth'], SettingsDAO(True,True,True,True,True))
        session.add(account)
        session.commit()
        session.refresh(account)
        session.close()
        return jsonify({'account_id':account.id}), 200

    @staticmethod
    def get(a_id):
        session = Session()
        account = session.query(AccountDAO).filter(AccountDAO.id == a_id).first()

        if account:
            settings_obj = account.settings

            text_out = {
                "customer_email": account.customer_email,
                "customer_password": account.customer_password,
                "customer_name": account.customer_name,
                "customer_address": account.customer_address,
                "customer_birth": account.customer_birth,
                "settings": {
                    "verification_code": settings_obj.verification_code,
                    "email_pref": settings_obj.email_pref,
                    "promotion_pref": settings_obj.promotion_pref,
                    "invoice_pref": settings_obj.invoice_pref,
                    "browser_pref": settings_obj.browser_pref
                }
            }
            session.close()
            return jsonify(text_out), 200

        else:
            session.close()
            return jsonify({"message": f"No account with email {email} was found or the password is incorrect"}), 404

    @staticmethod
    def delete(a_id):
        session = Session()
        effected_rows = session.query(AccountDAO).filter(AccountDAO.id == a_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({"message": f"No account with email ({email}) was found or the password is incorrect"}), 404
        else:
            return jsonify({'message': 'The account was removed'}), 200
