import uuid

from flask import session

from common.database import Database as db


class User():
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def get_by_email(cls, email):
        data = db.find_one("user", {"email": email})
        if data is not None:
            return cls(**data)
    @staticmethod
    def validate(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False
    @classmethod
    def register(cls,email,password):
        user = cls.get_by_email(email)
        if user is None:
            data = cls(email,password)
            data.save()
            session['email'] = None
            return True
        else:
            return False
    @staticmethod
    def login(email):
         session['email'] = email
    def json(self):
        return {
          "_id" : self._id,
          "email":self.email,
          "password" : self.password
        }
    @staticmethod
    def logout():
        session['email'] = None
    def save(self):
        db.insertData("user",self.json())