import pymongo
import certifi
from bson.objectid import ObjectId
# 連線到雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask,request,session
from flask import redirect

from flask import render_template
import json

uri = "mongodb+srv://root:love520wenyu@cluster0.woi4fe4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri,tlsCAFile=certifi.where())
db=client.member_system
app=Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/"    #靜態檔案對應的網址路徑
    )
app.secret_key="123"
@app.route("/")
def index():
    return render_template("index1.html")
@app.route("/member")
def member():
    if "name" in session:
        return render_template("member.html")
    else:
        return redirect("/")
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤,請聯繫客服")
    return render_template("error.html",message=message)
@app.route("/signup",methods=["POST"])
def signup():
    #從前端接受資料
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    #根據資料處理資料庫
    collection=db.user
    #尋找email是否已經使用過
    result=collection.find_one({
        "email":email
    })
    #如果有找到相同email則顯示已經註冊過
    if result!=None:
        return redirect("/error?msg=信箱已經被註冊")
    else:
        collection.insert_one({
            "name":name,
            "email":email,
            "password":password
        }
        )   
    return redirect("/")
@app.route("signin",methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user
    #檢查信箱密碼是否正確
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result==None:
        return redirect("/error?msg=信箱或密碼錯誤")
    session["name"]=result["name"]
    return redirect("/member")
@app.route("/signout")
def signout():
    del session["name"]
    return redirect("/")
app.run()