import tensorflow as tf
import tensorflow.contrib.distributions as tfd
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())
#%%
tf.enable_eager_execution()
#%%
A = tfd.Normal(0.,1.).sample([10000, 10, 10])
B = A @ A
