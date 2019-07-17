from pymongo import MongoClient
import gridfs

client = MongoClient(host="207.154.236.190", port=27017)

db = client.pista_test
fs = gridfs.GridFS(db)

path = r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp\handball\data.pkl"
with open(path, "rb") as f:
    a = fs.put(f, filename="data.pkl")
    

with fs.get(a) as obj:
    with open("e:/tmp.pkl", "wb") as out_file:
        out_file.write(obj.read())
      
##### zipping and unzipping
#%%
import shutil
shutil.make_archive("e:/tmp2", "zip", r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp")      

#%%
from zipfile import ZipFile

with ZipFile("e:/tmp.zip", 'w') as zf:
    zf.write(r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp\handball\data.pkl")

