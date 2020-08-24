import tensorflow as tf
import numpy as np
import pickle


def try_pickle(x):
    print(f"original: {x}")
    s = pickle.dumps(x)
    y = pickle.loads(s)
    print(f"pickled: {y}")


#%%

try_pickle(tf.constant([1., 1]))
try_pickle(tf.SparseTensor(indices=[[1, 1]], values=[2.], dense_shape=[2, 3]))