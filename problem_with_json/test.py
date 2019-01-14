Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> import collections
>>> Point = collections.namedtuple("Point", ["x", "y"])
>>> p = Point(1, 2)
>>> json.dumps(p)
'[1, 2]'
>>> type(p)
<class '__main__.Point'>
>>> def serialize(obj):
	if isinstance(obj, Point):
		return {"x": obj.x, "y": obj.y}
	else:
		return obj.__dict__

	
>>> json.dumps(p, default = serialize)
'[1, 2]'
>>> serialize(p)
{'x': 1, 'y': 2}
>>> class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		return super().default(serialize(obj))

	
>>> json.dumps(p, cls = MyEncoder)
'[1, 2]'
>>> def serialize(obj):
	print("uuu")
	if isinstance(obj, Point):
		return {"x": obj.x, "y": obj.y}
	else:
		return obj.__dict__

	
>>> 
>>> json.dumps(p, default = serialize)
'[1, 2]'
>>> 
