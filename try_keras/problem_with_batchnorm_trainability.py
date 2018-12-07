import keras
import keras.layers as kl
import numpy as np
import numpy.random as rnd

print(f"keras.__version__ == {keras.__version__}")

######
## Create as simple model containing a `BatchNormalization` layer `bn_layer`

inp = kl.Input([2])
y = inp
y = kl.Dense(2)(y)
bn_layer = kl.BatchNormalization()
y = bn_layer(y)
y = kl.ReLU()(y)
y = kl.Dense(1)(y)

model = keras.Model(inputs = inp, outputs = y)

######
## fix `bn_layer` and compile

bn_layer.trainable = False
model.compile(loss='mean_squared_error', optimizer='adam')


######
## train

print("Weights of Batch-normalization before training:")
print(*bn_layer.get_weights())

n = 100
model.fit(
    x = rnd.normal(size = [n, 2]),
    y = rnd.normal(size = [n, 1]),
    epochs = 10, 
    verbose = 0
)

print("Weights of Batch-normalization after training:")
print(*bn_layer.get_weights())
