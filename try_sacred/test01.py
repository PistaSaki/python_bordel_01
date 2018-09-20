from sacred import Experiment

ex = Experiment()

#@ex.config
#def my_config_01():
#    """This is `my_config_01`."""
#    
#    a = 10 # some integer
#    
#    # a dictionary
#    foo = {
#        "a_squared": a**2,
#        "bar": "uuu{}".format(a)
#    }
#    
#    if a > 8:
#        # cool: dynamic entry
#        e = a/2
#        
#ex.add_config("conf_01.yaml")
#
#@ex.named_config
#def basket_standard():
#    """This is standard basket config."""
#    max_pts = 150

@ex.automain
def my_main(a, _config):
    print('Hello world!')
    print("a = ", a)
    print("_config =", _config)
