import tensorflow as tf

@tf.function
def fun(a):
    print("retracing")
    return a + 1


for x in range(10):
    print(fun(tf.constant(x)))

for x in range(10):
    print(fun(x))


###
@tf.function
def gun(dic):
    print("retracing")
    return dic["x"] + 1


for x in range(10):
    dic = {"x": tf.constant(x)}
    print(gun(dic))
