from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)
client=MongoClient('mongodb://avanzo_user:isis2503@34.133.28.111:27017')





"""
class Empresa(db.Document):
    name=mongo.StringField()
    nit=db.IntField()
    def to_json(self):
        return {"name":self.name,
                "nit":self.nit}
"""



@app.route("/", methods=["GET"])
def index():
    db=client.empresas
    data=[]
    #data=db.find({})
    result= [
        {"name":"Apple","nit":12345},
        {"name":"Google","nit":12346},
        {"name":"Microsoft","nit":12347},
    ]
    for empresa in data:
        valor={
            "name":empresa["name"],
            "nit":empresa["nit"]
        }
        result.append(valor)
    return render_template("index.html",empresas=result)

if __name__=="__main__":
    app.run(debug=True)