import tensorflow as tf

#%%%
## Tensorflow official example from
## https://www.tensorflow.org/beta/guide/saved_model
#%%
class CustomModule(tf.Module):

    def __init__(self):
        super(CustomModule, self).__init__()
        self.v = tf.Variable(1.)
    
    @tf.function
    def __call__(self, x):
        return x * self.v
    
    @tf.function(input_signature=[tf.TensorSpec([], tf.float32)])
    def mutate(self, new_v):
        self.v.assign(new_v)
        return self.v
    
    @tf.function(input_signature=[tf.TensorSpec([], tf.float32)])
    def info(self, dummy):
        return {
            "aa": tf.constant([10], dtype=tf.float32),
            "bb": tf.constant([11], dtype=tf.float32),
        }




module = CustomModule()
#%%
module(tf.constant(0.))
signatures = {
    "serving_default": module.__call__.get_concrete_function(tf.TensorSpec(None, tf.float32)),
    "mutate": module.mutate,
    "info": module.info
}

tf.saved_model.save(module, "d:/tmp/module_with_signature/1", signatures=signatures)
#%%
# For serving run in command line
# docker run -t --rm -p 8501:8501 -v "d:/tmp/module_with_signature:/models/pista" -e "MODEL_NAME=pista" tensorflow/serving
#%%
## If the server runs you can try the following
import requests
resp = requests.get(url= r"http://localhost:8501/v1/models/pista/metadata")
print(resp.json())

#%%
url= r"http://localhost:8501/v1/models/pista:predict"

resp = requests.post(
    url=url,
    json={"signature_name": "mutate", "instances": [{"new_v": 3}]}
)
print("First change `v` =", resp.json())

resp = requests.post(
    url=url,
    json={"instances": [{"x": 2}]},
)
print("Then calculate `v *2`:", resp.json())
#%%
resp = requests.post(
    url=url,
    json={"signature_name": "info", 
         "instances": [{"dummy": 5}]
         }
)
print("info =", resp.json())
