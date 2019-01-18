class FileItem:
    def __init__(self, fname):
        self.fname = fname
        
        
f  = FileItem("/foo/bar")


## If a class is a child of `tuple`, its serialization can not be overriden.
from collections import namedtuple
Obj1 = namedtuple("Obj", ['cat', 'x', 'y'])

class Obj2:
    def __init__(self, cat, x, y):
        self.cat = cat
        self.x = x
        self.y = y

obj1 = Obj1("aa", 1, 2)
obj2 = Obj2("bb", 1, 2)


### custom encoding 
import json 
from json import JSONEncoder

class MyEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, FileItem):
                return {"path": o.fname}
            if isinstance(o, (Obj1, Obj2)):
                return {"cat": o.cat}
                
            #return o.__dict__    

## several ways to call it
print(MyEncoder().encode([f, obj1, obj2]))
print(json.dumps([f, obj1, obj2], cls = MyEncoder))
print(json.dumps([f, obj1, obj2], default = MyEncoder().encode))