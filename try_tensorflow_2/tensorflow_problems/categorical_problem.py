import numpy as np
import tensorflow as tf
from tensorflow import Tensor
from tensorflow_probability import distributions as tfd

floatx = np.float32

def get_probs_tensor(mu: Tensor) -> Tensor:
    """Return discretized normal distribution probas."""
    x = tf.range(10, dtype=floatx)
    f = (x-mu)**2 / 2
    f = f - tf.reduce_max(f)
    f = tf.exp(-f)
    f = f /  tf.reduce_sum(f)    
    return f

#%%
def get_distr(mu: Tensor) -> tfd.Categorical:
    """Return discretized normal distribution"""
    probs = get_probs_tensor(mu) 
    return tfd.Categorical(probs=probs)

mu = tf.Variable(15., dtype=floatx)

#%%
with tf.GradientTape() as tape:
    distr = get_distr(mu)
    l = distr.log_prob(0)
    
dl = tape.gradient(l, mu)
print(l, dl)

#%%
with tf.GradientTape() as tape:
    distr = get_distr(mu)
    l = tf.math.log(distr.probs[0])
    
dl = tape.gradient(l, mu)
print(l, dl)


