from flask import Flask, json , request, Response
from resources.db_util import DBUtil

def store_history(request):
	db_util = DBUtil()
	search = request.args()
	db_util.add_data_records('history-db', search)