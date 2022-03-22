from flask import Flask, json , request, Response
from resources.db_util import DBUtil

def store_history(request):
	request_json = request.get_json(silent=True)
	# request_args = request.args
	if request and 'arg1' in request_json:
		arg1 = request_json['arg1']
	elif request_args and 'arg1' in request_args:
		arg1 = request_args['arg1']
	else:
		arg1 = 'Invalid search'
	if arg1 != 'Invalid search':
		db_util = DBUtil()
		db_util.add_data_records('history-db', arg1)
	return arg1