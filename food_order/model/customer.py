import uuid

from common.database import Database
from model.user import User

class Customer():
    def __init__(self,uid,customer_name,item,_id=None):
        self.customer_name = customer_name
        self.item = item
        self._id = uuid.uuid4().hex if _id is None else _id
        self.uid = uid
    def save(self):
        Database.insertData("save_data",self.json())
    def json(self):
        return {
            "_id": self._id,
            "customer_name": self.customer_name,
            "items":[self.item],
            "uid":self.uid
        }
    @classmethod
    def add_items(cls,uid,customer_name,item):
        data = cls(uid,customer_name,item)
        data.save()
    @classmethod
    def get_item(cls,uid):
        l = []
        for i in Database.find('save_data',{"uid":uid}):
            l.append(i)
        return l


