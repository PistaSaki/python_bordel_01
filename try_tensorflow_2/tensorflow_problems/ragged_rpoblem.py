import tensorflow as tf

b = tf.ragged.constant([[1, 2], [3]], tf.float32)
a = tf.constant(5.0, tf.float32) 
print(a + b)

