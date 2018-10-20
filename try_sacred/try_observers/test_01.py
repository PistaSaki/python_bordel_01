"""
try adding artifacts
"""
import sacred
import numpy as np
import matplotlib.pyplot as pl
import os 
import sys

ex = sacred.Experiment()
ex.observers.append(sacred.observers.MongoObserver.create())
ex.observers.append(sacred.observers.FileStorageObserver.create("d:/tmp3"))

@ex.config
def test_config():
    a = 1
    b = 0
    c = 0
    x0 = 1
    
@ex.capture
def f(x, a, b, c):
    return a * x**2 + b * x + c

@ex.capture
def get_plot(a, b, c):
    fig, ax = pl.subplots()
    xxx = np.linspace(-1, 1, 100)
    ax.plot(xxx, f(xxx, a, b, c))
    
    return fig
    

@ex.automain
def main(a, b, c):
    print(f"Our function is {a} x**2 + {b} x + {c}")
    
    fig_path = "d:/tmp/pic_01.png"
    get_plot().savefig(fig_path)
    ex.add_artifact(fig_path)
    
    fig_path = "d:/tmp/pic_01.png"
    get_plot(b = 1).savefig(fig_path)
    ex.add_artifact(fig_path)
    
    ex.log_scalar("current_a", value = a, step=1)
    a += 1
    ex.log_scalar("current_a", value = a, step=2)
    
    return {
        "x": 10, "y": {"z": [1, 2], "txt": "Hello World"}
    }

#    ######
#    ## try put folder as artifact
#    ## it fails
#    
#    folder = "d:/tmp/test_folder"
#    if not os.path.exists(folder):
#        os.makedirs(folder)
#    
#    get_plot().savefig(os.path.join(folder, "pic_03.png"))
#    get_plot().savefig(os.path.join(folder, "pic_04.png"))
#    ex.add_artifact(folder, r"test_folder")
#    