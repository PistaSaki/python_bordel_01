import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Layer

#### Subclassing `Layer`
class L(Layer):
    def __init__(self):
        super().__init__()
        self.a = tf.Variable(3., name="a")

l = L()
print("When subclassing `Layer`, everything works:")
print(" -- l.weights =", l.weights)
print(" -- l.get_weights =", l.get_weights())

#### the same with `Model` instead of `Layer`
class M(Model):
    def __init__(self):
        super().__init__()
        self.a = tf.Variable(3., name="a")

m = M()
print()
print("When subclassing `Model`, `get_weights` does not work as expected:")
print(" -- m.weights =", m.weights)
print(" -- m.get_weights =", m.get_weights())

print()
print("More importantly, `m.save_weights` suffers from the same problem.")
