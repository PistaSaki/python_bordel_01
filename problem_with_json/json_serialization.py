class FileItem:
    def __init__(self, fname):
        self.fname = fname
        
        
f  = FileItem("/foo/bar")

from collections import namedtuple
Obj = namedtuple("Obj", ['cat', 'x', 'y'])

class Obj:
    def __init__(self, cat, x, y):
        self.cat = cat
        self.x = x
        self.y = y

obj = Obj("aa", 1, 2)


from json import JSONEncoder
class MyEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, FileItem):
                return {"path": o.fname}
            if isinstance(o, Obj):
                return {"cat": o.cat}
                
            #return o.__dict__    

print(MyEncoder().encode([f, obj]))