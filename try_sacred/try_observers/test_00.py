"""
this is the example from the official documentation
"""
import sacred

ex = sacred.Experiment()
ex.observers.append(sacred.observers.MongoObserver.create())

@ex.config
def test_config():
    a = 10

@ex.automain
def main(a):
    print(f"a = {a}")
