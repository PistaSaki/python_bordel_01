from pymongo import MongoClient
from pymongo.database import Database
from bson.objectid import ObjectId
import gridfs
from tempfile import TemporaryDirectory
import shutil
from pathlib import Path
from typing import Dict
from time import sleep

def _zip_and_upload_to_gridfs(db:Database, path:str, info:Dict) -> ObjectId:
    fs = gridfs.GridFS(db)
    
    
    with TemporaryDirectory() as tmpdir:
        zip_path = Path(tmpdir) / "tmp.zip"
        shutil.make_archive(Path(tmpdir) / "tmp", "zip", path)
        
        with open(zip_path, "rb") as zip_file:
            _id = fs.put(zip_file, name=name or Path(path).name)
            
    return _id


def _get_db(db:str, host:str="localhost", port:int=27017) -> Database:
    client = MongoClient(host=host, port=port)
    return client[db]
    

def upload(path:str, db:Database,  
           name:str=None, info:Dict=dict()) -> None:
    
    file_id = _zip_and_upload_to_gridfs(db, path, name)
    
    info = info.copy()
    if "name" not in info:
        info["name"] = name or Path(path).name
    
    info["file_id"] = file_id    
    print(info)
    
    col = db["files_info"]
    col.insert_one(info)
    
        
        
#%%

path = r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data"
db = _get_db("training_data")
upload(path, db, info={"project": "test", "version": 0})

#%%


#%%
path = Path(path)
with open(path, "rb") as f:
    a = fs.put(f, filename="data.pkl")
    

with fs.get(a) as obj:
    with open("e:/tmp.pkl", "wb") as out_file:
        out_file.write(obj.read())
      
##### zipping and unzipping
#%%
shutil.make_archive("e:/tmp2", "zip", r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp")      

#%%
from zipfile import ZipFile

with ZipFile("e:/tmp.zip", 'w') as zf:
    zf.write(r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data\tmp\handball\data.pkl")

