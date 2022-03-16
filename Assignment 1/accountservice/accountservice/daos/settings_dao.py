from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean

from db import Base

class SettingsDAO(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    verification_code = Column(Boolean, default=True)
    email_pref = Column(Boolean, default=True)
    promotion_pref = Column(Boolean, default=True)
    invoice_pref = Column(Boolean, default=True)
    browser_pref = Column(Boolean, default=True)

    def __init__(self, verification_code, email_pref, promotion_pref, invoice_pref, browser_pref):
        self.verification_code = verification_code
        self.email_pref = email_pref
        self.promotion_pref = promotion_pref
        self.invoice_pref = invoice_pref
        self.browser_pref = browser_pref