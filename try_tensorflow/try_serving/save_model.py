import tensorflow as tf

x = tf.placeholder(tf.float32, shape=[], name="x")
y = 2 * x + 3
init = tf.global_variables_initializer()

with tf.Session() as sess:
    print("if x = 10, y =", sess.run(y, {x: 10}))

#%%
## Saving
from pathlib import Path
MODEL_DIR = Path("d:/tmp22")
version = 1
export_path = MODEL_DIR / str(version)

with tf.Session() as sess:
    tf.saved_model.simple_save(
        session = sess,
        export_dir = str(export_path),
        inputs = {'x': x},
        outputs ={'y': y}
    ) 
    
print("saved to", export_path)
