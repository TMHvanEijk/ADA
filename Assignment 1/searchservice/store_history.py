from resources.db_util import DBUtil
from flask import Flask, json , request, Response

db_util = DBUtil()

def store_history(request):
	search = request.args()
	content = [{"search": search}]
	df = db_util.add_data_records('history_db', content)
	