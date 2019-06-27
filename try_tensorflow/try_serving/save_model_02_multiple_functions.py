"""
For serving the model follow the following steps:

1. Run this script. It will create dir "d:/tmp22/" and export the model there.

2. run ```
docker run -t --rm -p 8501:8501 -v "d:/tmp22:/models" -e "MODEL_NAME=pista" tensorflow/serving
```

3. use POST requests for calculating results. The URL is allways the same
`localhost:8501/v1/models/pista:predict`
The body is a JSON for instance:
```
{
	"signature_name": "both_yz",
	"instances": [
		{"x": 2}
	]
}
```
If you want to calculate only `y`, specify `"signature_name": "only_y"`.

REMARK: You can check the supported signatures by running 
```
saved_model_cli show --dir {export_path} --all
```
in the command line.

"""
#%%
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=[], name="x")
y = 2 * x + 3
z = x + 1

with tf.Session() as sess:
    print("if x = 10, y =", sess.run(y, {x: 10}))

#%%
## Saving
from pathlib import Path
from tensorflow import Tensor
from tensorflow.core.protobuf.meta_graph_pb2 import SignatureDef
from typing import Dict


MODEL_DIR = Path("d:/tmp22/pista")
version = 1
export_path = MODEL_DIR / str(version)

sess = tf.InteractiveSession()

def _sig_def(inputs: Dict[str, Tensor], outputs:Dict[str, Tensor]) -> SignatureDef:
    return tf.saved_model.signature_def_utils.build_signature_def(
        inputs = {k: tf.saved_model.utils.build_tensor_info(v) for k, v in inputs.items()},
        outputs = {k: tf.saved_model.utils.build_tensor_info(v) for k, v in outputs.items()},
        method_name = tf.saved_model.signature_constants.PREDICT_METHOD_NAME
    )

builder = tf.saved_model.builder.SavedModelBuilder(str(export_path))

builder.add_meta_graph_and_variables(
        sess = sess,
        tags = [tf.saved_model.tag_constants.SERVING],
        signature_def_map={
            'only_y': _sig_def({"x": x}, {"y": y}),
            'only_z': _sig_def({"x": x}, {"z": z}),
            'both_yz': _sig_def({"x": x}, {"y": y, "z": z}),
        }
    )

builder.save()
    
print("saved to", str(export_path))
