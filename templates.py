from flask import Flask,request
from flask import redirect
from flask import render_template
import json
app=Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/"    #靜態檔案對應的網址路徑
    )
@app.route("/")
def getSum():
    return render_template("index.html")
@app.route("/two")
def two():
    return render_template("two.html",name="小名")
@app.route("/calculate",methods=["POST"]) 
def calculate():
    #接收 GET 方法的字串
    #max=request.args.get("max","")
    #接收 POST 方法的字串
    max=request.form["max"]
    max=int(max)
    #寫一個小計算
    result=0
    for i in range(1,max+1):
        result+=i
    return render_template("result.html",data=result)    
app.run()