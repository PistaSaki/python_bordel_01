from pymongo import MongoClient
from pymongo.database import Database
from bson.objectid import ObjectId
import gridfs
from tempfile import TemporaryDirectory
import shutil
from pathlib import Path
from typing import Dict

def zip_and_upload(db:Database, path:str, info:Dict) -> ObjectId:
    count = db.fs.files.count_documents(info)
    assert count == 0, f"There are already {count} documents satisfying {info}."

    fs = gridfs.GridFS(db)
    with TemporaryDirectory() as tmpdir:
        zip_path = Path(tmpdir) / "tmp.zip"
        shutil.make_archive(Path(tmpdir) / "tmp", "zip", path)
        
        with open(zip_path, "rb") as zip_file:
            _id = fs.put(zip_file, **info)
            
    return _id

def download_and_unzip(db:Database, out_dir:str, info:Dict) -> None:
    count = db.fs.files.count_documents(info)
    assert count == 1, f"There are {count} documents satisfying {info}."
    _id = db.fs.files.find_one(info)['_id']
    
    fs = gridfs.GridFS(db)
    with TemporaryDirectory() as tmpdir:
        zip_path = Path(tmpdir) / "aaa.zip"
        with fs.get(_id) as obj:
            with open(zip_path, "wb") as zip_file:
                zip_file.write(obj.read())
                
        shutil.unpack_archive(zip_path, out_dir)

def _get_db(db:str, host:str=None, port:int=None) -> Database:
    client = MongoClient(host=host, port=port)
    return client[db]

if __name__ == "__main__":  
    #%%    
    path = r"E:\Pista\python_projects\workon_hrab2\bayes_sport_eager\data"
    db = _get_db("training_data")    
    #%%
    zip_and_upload(db, path, info={"project": "test", "version": 1})
    #%%
    download_and_unzip(db, out_dir="e:/tmp", info={"project": "test", "version": 1})
