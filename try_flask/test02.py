####
## Model
import tensorflow as tf

class Model:
    def __init__(self):
        self.floatX = tf.float32
        self.graph = tf.Graph()
        with self.graph:
            self.a = tf.placeholder(dtype=self.floatX, shape=[], name="a")
            self.b = tf.placeholder(dtype=self.floatX, shape=[], name="b")
            self.result = self.a + self.b
            
    def __call__(self, a:float, b:float) -> float:
        with self.graph, tf.Session() as sess:
            feed_dict = {self.a: a, self.b: b}
            return sess.run(self.result, feed_dict)
            
        
            
    

#############################################
####
## View 
from flask import Flask
from flask_restful import Api, Resource, reqparse

class FlaskView(Resource):
    def get(self, a):
        return f"Hello {a}!"
        

if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(FlaskView, "/user/<int:a>&<int:b>")
    app.run(debug=True)