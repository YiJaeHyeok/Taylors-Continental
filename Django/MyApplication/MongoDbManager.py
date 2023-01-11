import pymongo
 
class MongoDbManager:
    _instance = None
    client = pymongo.MongoClient(host='localhost',
                                port=27017)
    database = client['MyApplicationDB']['MyApplicationCollection']
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
 
    def get_users_from_collection(cls, query):
        assert cls.database
        return cls.database.find(query)
 
    def add_user_on_collection(cls, data):
        if type(data) is list:
            return cls.database.insert_many(data)
        else :
            return cls.database.insert_one(data)