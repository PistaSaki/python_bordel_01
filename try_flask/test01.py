from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = {
    "Pista": {
     "name": "Pista",
     "age": 42,    
    },
    "Timea":{
     "name": "Timea",
     "age": 33,
    },
}
    
count = 0

class User(Resource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        global count
        count += 1
        self.id = count
    
    def get(self, name):
        try:
            user = dict(users[name])
            user["instance_id"] = self.id
            return user, 200
        
        except KeyError:
            return "User not found", 404
        

if __name__ == "__main__":
    api.add_resource(User, "/user/<string:name>")
    app.run(debug=True)