from flask import Flask
from flask_restful import Api, Resource, abort
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser

app = Flask(__name__)
api = Api(app)

class Foo(Resource):
    args = {
        'bar': fields.Str(
            required=True,
            validate=validate.OneOf(['baz', 'qux']),
        ),
    }

    @use_kwargs(args)
    def get(self, bar):
        return {'bar': bar}

api.add_resource(Foo, '/foo', endpoint='foo')

# This error handler is necessary for usage with Flask-RESTful.
@parser.error_handler
def handle_request_parsing_error(err):
    abort(422, errors=err.messages)

if __name__ == '__main__':
    app.run(debug=True)