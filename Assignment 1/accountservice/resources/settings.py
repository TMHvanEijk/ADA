from flask import jsonify
from daos.account_dao import AccountDAO
from db import Session

class Settings:
    @staticmethod
    def update(a_id, email, password, verification_code, email_pref, promotion_pref, invoice_pref,
               browser_pref):
        session = Session()
        #account = session.query(AccountDAO).filter((AccountDAO.customer_email == email) & (AccountDAO.customer_password == password))[0]
        account = session.query(AccountDAO).filter((AccountDAO.customer_email == email) & (AccountDAO.customer_password == password))[0]

        account.settings.verification_code = verification_code
        account.settings.email_pref = email_pref
        account.settings.promotion_pref = promotion_pref
        account.settings.invoice_pref = invoice_pref
        account.settings.browser_pref = browser_pref
        session.commit()

        return jsonify({"message" : "The settings were changed"}), 200