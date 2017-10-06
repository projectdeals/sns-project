import uuid

from common.database import Database

class Item():
    def __init__(self,item_name,description,price,_id=None):
        self.item_name =  item_name
        self.price= price
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    @staticmethod
    def get_items():
        l =[]
        item = Database.find("item",{})
        for i in item:
            l.append(i)
        return l
