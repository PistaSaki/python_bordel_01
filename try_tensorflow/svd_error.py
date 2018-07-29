import numpy as np
import numpy.linalg as la
import tensorflow as tf

## choose our matrix
A = np.array([
        [ 10, -10],
        [-45, -41],
    ],
    dtype = np.float32      
)

## a method for checking the SVD of A
def check_USV(U, S, V):
    reconstruction = U @  np.diag(S) @ V
    print( reconstruction )
    print("error =", np.max(np.abs(A - reconstruction)))
    
#############
## Numpy SVD

U, S, V = la.svd(A)

print("  NUMPY:")
check_USV(U, S, V)

############
## Tensorflow SVD

## tensorflow.svd has different ordering of outputs 
s, u, v = tf.svd(tf.constant(A), full_matrices=True)

with tf.Session() as sess:
    U_tf, S_tf, V_tf =  sess.run([u, s, v])

print("\n  TENSORFLOW:")
check_USV(U_tf, S_tf, V_tf)