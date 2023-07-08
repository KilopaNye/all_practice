from flask import Flask
app=Flask(__name__)#代表目前執行的目錄


@app.route("/")
def home():
    return "Hello Flask"
