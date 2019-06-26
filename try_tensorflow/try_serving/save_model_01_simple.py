"""
For serving the model follow the following steps:

1. Run this script. It will create dir "d:/tmp22/" and export the model there.

2. run ```
docker run -t --rm -p 8501:8501 -v "d:/tmp22:/models" -e "MODEL_NAME=pista" tensorflow/serving
```

3. use POST requests for calculating results. The URL is 
`localhost:8501/v1/models/pista:predict`
The body is a JSON for instance:
```
{
	"instances": [
		{"x": 2}
	]
}
```

"""
#%%
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=[], name="x")
y = 2 * x + 3

with tf.Session() as sess:
    print("if x = 10, y =", sess.run(y, {x: 10}))

#%%
## Saving
from pathlib import Path
MODEL_DIR = Path("d:/tmp22/pista")
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
