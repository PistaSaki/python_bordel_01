"""
Try dependencies. Run in console with:
python -m test02 print_dependencies with a=2
"""

import sacred

import sys
sys.path.append("../../test_package")
import test_package
from test_package import fun 

experiment = sacred.Experiment()
experiment.add_package_dependency(
    package_name = test_package.__name__,
    version = "1.0.0"
)


@experiment.config
def my_config_01():
    """This is `my_config_01`."""
    
    a = 10 # some integer

@experiment.automain
def my_main(a, _config):
    print('Hello world!')
    print(f"a = {a}, fun(a) = {fun(a)}" )
    print("_config =", _config)
