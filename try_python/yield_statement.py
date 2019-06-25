def aaa():
    print("starting")
    yield 1
    print("finish")
    
g = aaa()
print("call next first time")
print(next(g))
print("call next second time")
try: 
    next(g)
except StopIteration as e:
    print("raised exception of class", type(e))