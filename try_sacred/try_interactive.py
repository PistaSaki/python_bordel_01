from sacred import Experiment

ex = Experiment("test_sacred", interactive=True)

@ex.config
def config1():
    a = 10

@ex.main
def main(a):
    print(f"runing_experiment with a= {a}")    
#%%

ex.run()
ex.run(config_updates={"a":11})
