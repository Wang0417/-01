from flask import Flask,request
from flask import redirect
import json
from flask import session
app=Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/"    #靜態檔案對應的網址路徑
    )
#設定session先設定KEY
app.secret_key="123"
#網站首頁
@app.route("/") 
def index():
    return "你好"
#使用 GET 方法處理路徑
@app.route("/hello")
def hello():
    name=request.args.get("name","")
    session["user"]=name #session["欄位名稱"]=資料 
    return "你好"+name
@app.route("/talk")
def talk():
    name=session["user"]
    return "who are you?"+name

app.run(port=3000)