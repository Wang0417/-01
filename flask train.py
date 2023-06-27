from flask import Flask,request
from flask import redirect
import json
app=Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/"    #靜態檔案對應的網址路徑
    )
#利用要求字串提供彈性
@app.route("/getSum")
def getSum():
    max=request.args.get("max",100)#接收字串?(Query String)
    max=int(max)#先把字串轉數字才能做處理
    result=0
    for i in range(1,101):
        result+=i
    return "結果:"+str(result)    

#建立路徑/對應的處理函式
    #print("請求方法",request.method)
    #print("通訊協定",request.scheme)
    #print("主機名稱",request.host)
    #print("路徑",request.path)
    #print("完整的網址",request.url)
    #print("遊覽器和作業系統",request.headers.get("user-agent"))
    #print("語言偏好",request.headers.get("accept-language"))
    #print("引薦網址",request.headers.get("referrer"))
    
@app.route("/") 
def index():
    lang=request.headers.get("accept-language")#讀取蒐尋器的語言
    if lang.startswith("en"):#如果蒐尋器的語言是英文
        return json.dumps({   #把字典轉成json
            "status":"ok",
            "text":"Hello"
        })
    else:
        return json.dumps({
            "status":"ok",
            "text":"你好"
        },ensure_ascii=False)#不使用ascii轉換中文

    

@app.route("/data/<data>")#接收變數
def data(data):
    return "one"+data

#重新導向
@app.route("/redirect")
def respond():#重新導向到其他網址
    return redirect("https://www.youtube.com/watch?v=p5RoBuO3tSc&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=7")
    
app.run(port=3000)