from pymongo import MongoClient
import gridfs

client = MongoClient(host="207.154.236.190", port=27017)

db = client.pista_test
fs = gridfs.GridFS(db)

path = r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp\handball\data.pkl"
with open(path, "rb") as f:
    a = fs.put(f, filename="data.pkl", info="whatever")
    

with fs.get(a) as obj:
    with open("e:/tmp.pkl", "wb") as out_file:
        out_file.write(obj.read())
