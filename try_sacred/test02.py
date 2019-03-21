import sacred

ex = sacred.Experiment()

@ex.config
def my_config_01():    
    a = 10 # some integer
    
    # a dictionary
    foo = {
        "a_squared": a**2,
        "bar": "uuu{}".format(a)
    }
    
    if a > 8:
        # cool: dynamic entry
        e = a/2

@ex.config
def my_config_01(foo, a):
    foo["a_cubed"] = a**3

@ex.automain
def my_main(a, _config):
    print('Hello world!')
    print("a = ", a)
    print("_config =", _config)
