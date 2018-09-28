"""
Try dependencies. 
There are two versions:
    - the package has been installed via pip
    - you import it from a local dir not using pip

Run in console with:
python -m try_dependencies_01 print_dependencies with a=2
"""

import sacred
experiment = sacred.Experiment()

### if the package has been installed via pip then just import and use it:
import test_package as tp

### If jou import it from your local directory, you must add the path:
#import sys
#sys.path.append("../../test_package")
#import test_package as tp

experiment.add_package_dependency(
    package_name = tp.__name__,
    version = tp.__version__
)


@experiment.config
def my_config_01():
    """This is `my_config_01`."""
    
    a = 10 # some integer

@experiment.automain
def my_main(a, _config):
    print('Hello world!')
    print(tp.fun(a))
    print(f"a = {a}, fun(a) = {tp.fun(a)}" )
    print("_config =", _config)
