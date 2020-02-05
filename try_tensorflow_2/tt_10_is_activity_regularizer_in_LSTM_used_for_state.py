"""I don't know yet whether the activity regularization is used also on states"""
#%%
from tensorflow.keras import layers as kl
from tensorflow import keras
import tensorflow as tf
#%%
def to_numbers(x):
    if isinstance(x, list):
        return [to_numbers(y) for y in x]
    return x.numpy().tolist()

#%%
l = kl.GRU(
    units=2, activity_regularizer="l2", stateful=True,
    kernel_initializer="zeros"
    )
model = keras.Sequential([l])
model(tf.ones([1, 3, 2])) ## build
#%%
print('output:',  to_numbers(model(tf.ones([1, 3, 2]))))
print('states:', to_numbers(l.states))
print('losses:', to_numbers(l.losses))
