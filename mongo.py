import pymongo
import certifi
# 連線到雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://root:love520wenyu@cluster0.woi4fe4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri,tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
#選擇操作的資料庫(mywebsite)
db=client.mywebsite
collection=db.users#選擇要操作的集合
# 把1個資料放進資料庫
result=collection.insert_one({
    
    "name":"老版",
    "email":"h1@h1.com",
    "gender":"男生",
    "level":2
})
###新增多筆資料
result2=collection.insert_many([{
    
    "name":"老張",
    "email":"b1@b1.com",
    "gender":"男生",
    "level":2
},{
    
    "name":"老許",
    "email":"d1@d1.com",
    "gender":"男生",
    "level":2
},
])
print("資料新增成功")
#印出加入一筆資料的ID
print(result.inserted_id)
#印出加入多筆資料的id
print(result2.inserted_ids)