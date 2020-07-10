from flask import Flask
from flask_restful import Api
from Movies.resources.Profit import Profit


# creating the flask app
app = Flask(__name__)


# creating an API object
api = Api(app)

api.add_resource(Profit, '/movies/v1/profit')


# driver function
if __name__ == '__main__':
    app.run(debug=True)