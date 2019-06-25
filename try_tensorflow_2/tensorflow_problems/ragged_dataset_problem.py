import tensorflow as tf
from tensorflow.data import Dataset

data = tf.ragged.constant([
        [[1, 1],
         [2, 2]],
        
        [[3, 3]],
         
        [],
        
        [[4, 4],
         [5, 5]]
    ], dtype=tf.float32, ragged_rank=2)

ds = Dataset.from_tensor_slices(data)
ds = ds.batch(2)

for i, batch in enumerate(ds):
    print("batch", i)
    for x in batch:
        print(x)