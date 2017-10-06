import pymongo

class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    web = ""
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.web = client['food_shop']

    @staticmethod
    def insertData(collection,data):
        Database.web[collection].insert(data)

    @staticmethod
    def find(collection, data):
        return Database.web[collection].find(data)

    @staticmethod
    def find_one(collection, data):
        return Database.web[collection].find_one(data)

