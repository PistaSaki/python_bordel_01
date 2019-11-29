"""This is solved -- the problem is that when keras recieves observed Y of shape
Y.shape = [batch_len], then in `fit` it calls the loss-function with Y reshaped as
`[batch_len, 1]`. This caused some strange broadcasting that messed things up.
"""

import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from tensorflow_probability import distributions as tfd
from tensorflow.keras import layers as kl

#%%
## Consider linear regression problem
# X in R^3, Y in R
# X ~ Normal(0, 1)
# Y = Normal(W_true @ X, 1)
# where W_true in R^3 is unknown.

#%%
## Generate linear regression data
W_true = np.array([[1, 2, 3]]).T # true value we want to find
N = 1000 # sample size

tf.random.set_seed(1)
X = tfd.Normal(0, 10).sample(sample_shape = [N, 3]) # random regression matrix (inputs)
Y = tfd.Normal(X @ W_true, 1).sample()[:, 0]

#%%
## Model using tensorflow-probability
print("Find `W` using TFP:")

model_tfp = tf.keras.models.Sequential([
    kl.Dense(units = 1, use_bias = False),
    tfp.layers.DistributionLambda(lambda t: tfd.Normal(loc = t[... , 0], scale = 1))
])

def negloglik(x, rv_x): 
    x = tf.squeeze(x)
    tf.assert_rank(x, 1)    
    res = -rv_x.log_prob(x)
    tf.assert_rank(res, 1)
    return res
    

model_tfp.compile(optimizer='adam', loss=negloglik)
model_tfp.fit(x = X, y = Y, epochs = 5000, batch_size=1024, verbose=0) 
print(model_tfp.weights[0].numpy())
#%%
## Model using standard keras
print("Find `W` using keras:")

model_keras = tf.keras.models.Sequential([
    kl.Dense(units = 1, use_bias = False),
])

model_keras.compile(optimizer='adam', loss='mse')

model_keras.fit(x = X, y = Y, epochs = 5000, batch_size=1024, verbose=0) 
print(model_keras.weights[0].numpy())


#%%
## Optimization of `model_tfp` directly using tensorflow
print("Find `W` using TFP directly optimizing the loss:")
model = model_tfp

def get_loss():
    return tf.reduce_mean(negloglik(Y, model(X)))

optimizer = tf.optimizers.Adam() # the same optimizer as above

@tf.function
def train_step():
    with tf.GradientTape() as tape:
        loss = get_loss()

    grads = tape.gradient(loss, model.trainable_weights)
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    return loss

for i in range(10000):
    loss = train_step()
    
print(model.weights[0].numpy())

#%%
old_weights = model.get_weights()
model.set_weights([W_true])
get_loss()
#%%
tf.reduce_mean(-tfd.Normal(X @ W_true, 1).log_prob(Y))

#%%
#@title Synthesize dataset.
w0 = 0.125
b0 = 5.
x_range = [-20, 60]

def load_dataset(n=150, n_tst=150):
  np.random.seed(43)
  def s(x):
    g = (x - x_range[0]) / (x_range[1] - x_range[0])
    return 3 * (0.25 + g**2.)
  x = (x_range[1] - x_range[0]) * np.random.rand(n) + x_range[0]
  eps = np.random.randn(n) * s(x)
  y = (w0 * x * (1. + np.sin(x)) + b0) + eps
  x = x[..., np.newaxis]
  x_tst = np.linspace(*x_range, num=n_tst).astype(np.float32)
  x_tst = x_tst[..., np.newaxis]
  return y, x, x_tst

y, x, x_tst = load_dataset()