"""
this is the example from the official documentation
"""
from sacred import Experiment
ex = Experiment()

@ex.config
def test_config():
    a = 10

@ex.config_hook
def hook(config, command_name, logger):
    config.update({'hook': True})
    print(f"config = {config}")
    return config

@ex.automain
def main(hook, other_config):
    print(f"hook = {hook}")
