import pymongo

"""
dict1 = {'key': '2', 'value': '123456'}
dict2 = {'key': '2', 'value': '456789'}
增
m.connection().tablename('tablename').insert([dict1, dict2])
删
m.connection().tablename('tablename').delete({})
查
list=m.connection().tablename('tablename').find()
for x in list:
    print(x)
改
m.connection().tablename('tablename').updateOne({"value": "123456"}, {"$set": {"value": "123456789"}})
"""
class mongodb():
    def connection(self, conStr=None, database='test'):
        if conStr is None:
            conStr = 'mongodb://localhost:27017/'
        mClient = pymongo.MongoClient(conStr)
        self.mConn = mClient[database]
        return self

    def tablename(self,table=None):
        self.tableConn=self.mConn[table]
        return self

    def insert(self, dataDICT= None):
        if len(dataDICT) > 1:
            return self.tableConn.insert_many(dataDICT)
        return self.tableConn.insert_one(dataDICT)

    def find(self, where=None, filter=None):
        return self.tableConn.find(where, filter)


    def findOne(self, filter=None):
        return self.tableConn.find_one(filter=filter)

    def updateOne(self, olddict, newdict):
        return self.tableConn.update_one(olddict, newdict)

    def updateMany(self, olddict, newdict):
        return self.tableConn.update_many(olddict, newdict)

    def deleteOne(self, DICT):
        return self.tableConn.delete_one(DICT)

    def deleteMany(self, DICT):
        return self.tableConn.delete_many(DICT)

    def drop(self):
        self.tableConn.drop()




