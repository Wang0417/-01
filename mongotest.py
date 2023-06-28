import pymongo
import certifi
from bson.objectid import ObjectId
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
    "level":1
})
###新增多筆資料
result2=collection.insert_many([{
    
    "name":"老張",
    "email":"b1@b1.com",
    "gender":"男生",
    "level":3
},{
    
    "name":"老許",
    "email":"d1@d1.com",
    "gender":"男生",
    "level":2
},
])
#更新一筆資料的方法
result3=collection.update_one({
    #搜尋符合的資料
    "email":"p1@p1.com"
},{
    #要更新的方法 set設定 unset清除 inc 加 mul 乘
    
   "$set":{
       #更改的資料內容
     "name":"Wang jhenzhi"  
   } 
})
#更新多筆資料的方法
result4=collection.update_many({
    #搜尋符合的資料
    "level":2 
},{
    #要欄位更新的方法 set設定 unset清除 inc 加 mul 乘
    
   "$set":{
       #更改的資料內容
     "level":4
   } 
})
#刪除多筆資料的方法
result5=collection.delete_many({
    #搜尋符合的資料
    "level":3 
})
#篩選資料尋找資料單筆用find_one
result6=collection.find({
    #篩選邏輯條件 and or 也可以不用
    "$and":[
        {"name":"老闆"},
        {"level":4}
    ]
})
#篩選結果的排序
cur=collection.find({
    "$or":[
        {"level":4},
        {"name":"老闆"}
    ]}, sort=[#由大到小排序 由小到大AESCENDING
        ("level",pymongo.DESCENDING)
    ]
)
for doc in cur:
    print(doc)
#print("資料新增成功")
#印出加入一筆資料的ID
#print(result.inserted_id)
#印出加入多筆資料的id
#print(result2.inserted_ids)
#根據ObjectId尋找一個資料
#data=collection.find_one(ObjectId("649ab3a473fd29dc915ded06"))
#print(data)
#取得文件中的欄位(email)
#print(data["email"])
##更新資料
print("符合條件的文件數量",result4.matched_count)
print("實際更新的文件數量",result4.modified_count)
print("實際刪除的文件數量",result5.deleted_count)