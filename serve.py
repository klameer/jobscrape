from flask import Flask
from flask import render_template
from tinydb import TinyDB
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    db = TinyDB("myfile.json")
    data = db.all()
    ret_val = {"data" : data}
    return json.dumps(ret_val)

if __name__=="__main__":
    app.run(debug=True)
