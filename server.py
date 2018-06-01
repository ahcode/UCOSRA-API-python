from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return "hola"

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(port='5002')