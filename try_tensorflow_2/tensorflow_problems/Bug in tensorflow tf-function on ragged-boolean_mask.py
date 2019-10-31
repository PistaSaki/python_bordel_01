import tensorflow as tf

## Define some RaggedTensors
print("`a2` and `b2` are ragged tensors with batch-length = 2")
a2 = tf.ragged.constant([[1, 2, 3], [4, 5]], dtype=tf.float32, 
                       ragged_rank=1, inner_shape=tuple())
print("a2 =", a2)

b2 = tf.ragged.constant([[1], [2, 3]], dtype=tf.float32, 
                       ragged_rank=1, inner_shape=tuple())
print("b2 =", b2)

print("`a3` and `b3` are ragged tensors with batch-length = 3")
a3 = tf.ragged.constant([[1, 2, 3], [4, 5], [3]], dtype=tf.float32, 
                       ragged_rank=1, inner_shape=tuple())
print("a3 =", a3)

b3 = tf.ragged.constant([[1], [2, 3], [5]], dtype=tf.float32, 
                       ragged_rank=1, inner_shape=tuple())
print("b3 =", b3)

## Define a function
print("We define a function `fun` with `tf.ragged.boolean_mask`.")
def fun(x):
    maximums = tf.reduce_max(x, axis=1)
    mask = maximums > 4
    selection = tf.ragged.boolean_mask(x, mask)
    return tf.reduce_sum(selection)

## Run the function in eager-mode
print("Running in eager-mode.")
print("fun(a2) =", fun(a2))
print("fun(a3) =", fun(a3))
print("fun(b2) =", fun(b2))
print("fun(b3) =", fun(b3))

## Now running the same in graph-mode
fun = tf.function(fun, experimental_relax_shapes=True)

print("Running in graph-mode.")
print("fun(a2) =", fun(a2))
print("fun(a3) =", fun(a3))
print("fun(b2) =", fun(b2))
print("fun(b3) =", fun(b3))
