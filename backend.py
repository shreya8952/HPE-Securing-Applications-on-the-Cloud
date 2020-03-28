from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/add",methods=["POST"])
def addPerson():
    nameOfPerson = request.get_json()["nameOfPerson"]
    filee = open("db.json", "r+")
    data_read = json.loads(filee.read())
    data_read["persons"].append(nameOfPerson)
    filee.seek(0)
    filee.write(json.dumps(data_read))
    filee.truncate()
    filee.close()
    return {},200

@app.route("/",methods=["GET"])
def listPerson():
    filee = open("db.json", "r+")
    data_read = json.loads(filee.read())
    filee.close()
    return json.dumps(data_read["persons"]), 200

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")






    