from flask_restful import Resource
from flask import jsonify,make_response,request
from datetime import datetime 


class Profit(Resource):
	def find_max_profit(self,data):
		res=[]
		c=0

		if(len(data)==0):
			return None

		data_list_sorted=sorted(data,key = lambda d:datetime.strptime(d['end_date'],'%d %b'))

		for each_movie in data_list_sorted:
			if(len(res)==0):
				res.append(each_movie)
				c=c+1
			else:
				sd=datetime.strptime(each_movie['start_date'],'%d %b')
				ed=datetime.strptime(res[-1]['end_date'],'%d %b')
				if(sd>ed):
					res.append(each_movie)
					c=c+1
		return (c,res)


	def post(self):
		request_body = request.get_json()
		profit,res=self.find_max_profit(request_body)
		resp={}
		resp['profit']=profit
		resp['movies']=res
		return make_response(jsonify(resp),200)