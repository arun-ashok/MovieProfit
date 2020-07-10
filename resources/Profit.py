from flask_restful import Resource
from flask import jsonify,make_response,request


class Profit(Resource):

    def post(self):

    	request_body = request.get_json()
    	print(request_body)
    	return make_response("Request received",200)