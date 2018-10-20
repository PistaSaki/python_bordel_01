"""
Try dependencies. Run in console with:
python -m test02 print_dependencies with a=2
"""

import sacred

data_ingredient = sacred.Ingredient("data")
experiment = sacred.Experiment(ingredients=[data_ingredient])

@data_ingredient.config
def data_config():
    file = "aaa"

@experiment.config
def my_config_01():
    """This is `my_config_01`."""
    
    a = 10 # some integer

@experiment.automain
def my_main(a, _config):
    print('Hello world!')
    print("_config =", _config)
