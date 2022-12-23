from ..plugins.db import *
from sqlalchemy import Integer, String, DateTime, Column, Boolean
from sqlalchemy.sql import func
import logging

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=150), unique=True)
    email = Column(String(256))
    password = Column(String(length=256))
    created_at = Column(DateTime(timezone=True), default=func.now())
    email_verified = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.username}"

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception as error:
            logging.error(error)
            session.rollback()
    
    @classmethod
    def exists(cls, email):
        sql = f"""
            SELECT username, email, password from "user"
            WHERE email = '{email}';
        """
        try:
            result = tuple(session.execute(sql).first())
            if result:
                user = {
                    "username": result[0],
                    "email": result[1],
                    "password": result[2]
                }
                return user
        except Exception as error:
            logging.error(error)
    
    @classmethod
    def check_email(cls, email):
        sql = f"""
            SELECT email_verified FROM "user"
            WHERE email = '{email}'
        """
        result = tuple(session.execute(sql).first())
        return result[0]
    
    @classmethod
    def delete(cls, id: int):
        try:
            session.query(User).filter(User.id == id).delete()
            session.commit()
    
        except Exception as error:
            logging.error(error)
            return error
