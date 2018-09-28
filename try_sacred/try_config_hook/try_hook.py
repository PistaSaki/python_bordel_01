import sacred
import yaml

experiment = sacred.Experiment()


@experiment.config
def standard_config():
    a = 10 # some integer
    data_config = "data_config_01.yaml"
    
    
@experiment.config_hook
def update_data_config_from_file(config, command_name, logger):
    dc = config["data_config"]
    if isinstance(dc, str):
        print(f"Updating data_config from {dc}.")
        #config.update({"data_config": yaml.load(open(dc, "rt"))})
        config.update({
            "data_config": "updated",
            "hook": True
        })
        
    return config
        
        
@experiment.automain
def my_main(a, data_config, _config):
    print('Hello world!')
    print(f"a = {a}" )
    print(f"data_config = {data_config}" )
    print("_config =", _config)
