from tensorflow.keras import layers as kl
from tensorflow import keras
from tensorflow.keras.layers import Layer, Dense
import tensorflow as tf
from tensorflow.keras import regularizers

#%%
l = kl.Dense(10, kernel_regularizer="l2")
kl.serialize(l)
#%%
l1 = kl.deserialize({'class_name': 'Dense', 'config':{'units': 5}})
l1.get_config()
#%%
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object
deserialize_keras_object({'class_name': 'Dense', 'config':{'units': 5}}, module_objects=globals())

#%%
class ConstantMultiple(Layer):
    def __init__(self, init_val:float=1, regularizer=None, **kwargs):
        super().__init__(**kwargs)
        self.init_val = init_val
        self.regularizer = regularizers.get(regularizer)
        
        self.c = self.add_weight(name="c", shape=(), regularizer=regularizer)
        
    def call(self, input):
        return self.c * input
    
    def get_config(self):
        config = {
                "init_val": self.init_val,
                "regularizer": regularizers.serialize(self.regularizer)
            }
        base_config = super().get_config()
        return dict(list(base_config.items()) + list(config.items()))
    
    
c = ConstantMultiple(init_val=3, regularizer=regularizers.l2())
config = c.get_config()
config
#%%
d = ConstantMultiple.from_config(config)
d.get_config()
#%%
c1 = deserialize_keras_object({'class_name': 'ConstantMultiple', 'config':{'init_val': 5}}, module_objects=globals())
c1.get_config()