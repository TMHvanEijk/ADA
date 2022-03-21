from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.settings_dao import SettingsDAO
from daos.login_dao import LoginDAO
from db import Base

class AccountDAO(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    customer_email = Column(String)
    customer_password = Column(String)
    customer_name = Column(String)
    customer_address = Column(String)
    customer_birth = Column(String)

    settings_id = Column(Integer, ForeignKey('settings.id'))
    settings = relationship(SettingsDAO.__name__, backref=backref("account", uselist = False))
    login_id = Column(Integer, ForeignKey('login.id'))
    login = relationship(LoginDAO.__name__, backref=backref("account", uselist = False))
    
    def __init__(self, customer_email, customer_password, customer_name, customer_address, customer_birth, settings, login):
        self.customer_email = customer_email
        self.customer_password = customer_password
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_birth = customer_birth
        self.settings = settings
        self.login = login

