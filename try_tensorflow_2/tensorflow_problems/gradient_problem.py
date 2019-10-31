import numpy as np
from numpy import nan
import tensorflow as tf
from tensorflow import Tensor, RaggedTensor
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer
from tensorflow_probability import distributions as tfd
from typing import List

#%%
obs = np.array([1, nan, 2, 3, nan])
mu = tf.Variable(0.)
sigma = tf.Variable(1.)
#%%
def get_lhd(mu, sigma, obs):
    lhds = tfd.Normal(mu, sigma).prob(obs)
    lhds = tf.where(tf.math.is_finite(obs), lhds, 0) # get rid of nan observations
    return tf.reduce_sum(lhds)

get_lhd(mu, sigma, obs)
#%%
with tf.GradientTape() as tape:
    lhd = get_lhd(mu, sigma, obs)
#%%
tape.gradient(lhd, [mu, sigma])

#%%%
def normal_prob(mu, sigma, obs):
    coef = 1 / (2 * np.pi * sigma**2) ** (1/2) 
    return coef * tf.exp(- (obs - mu)**2 / (2 * sigma**2))    
######
## Try with my own function
def get_lhd(mu, sigma, obs):
    lhds = normal_prob(mu, sigma, obs)
    lhds = tf.where(tf.math.is_finite(obs), lhds, 0) # get rid of nan observations
    return tf.reduce_sum(lhds)

get_lhd(mu, sigma, obs)
#%%
with tf.GradientTape() as tape:
    lhd = get_lhd(mu, sigma, obs)
#%%
tape.gradient(lhd, [mu, sigma])
