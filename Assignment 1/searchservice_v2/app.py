from flask import Flask, json , request, Response
from store_history import store_history
import requests

from resources.db_util import DBUtil

app = Flask(__name__)
app.config["DEBUG"] = True
db_util = DBUtil()


@app.route('/searchservice/<table_name>', methods=['POST'])
def create_table(table_name):
    # get the payload or body
    req_data = request.get_json()
    columns = req_data['columns']
    db_util.create_tb(table_name, columns)
    return json.dumps({'message': 'a table was created'}, sort_keys=False, indent=4), 200


@app.route('/searchservice/<table_name>', methods=['DELETE'])
def delete_table(table_name):
    db_util.drop_tb(table_name)
    return json.dumps({'message': 'a table was dropped'}, sort_keys=False, indent=4), 200


@app.route('/searchservice/<table_name>', methods=['PUT'])
def update_data(table_name):
    content = request.get_json()
    db_util.add_data_records(table_name, content)
    return json.dumps({'message': '{} data were updated'.format(table_name)}, sort_keys=False, indent=4), 200


@app.route('/searchservice/<search>', methods=['GET'])
def read_data(search):
    # return json.dumps({'type of search': '{}'.format(type(search))})
    if search == 'history':
        df = db_util.read_data_records('history_db', search)
        resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    else:
        df = db_util.read_data_records('search_db', search)
        resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
        requests.post('https://us-central1-ada1search.cloudfunctions.net/store_history?arg1={}'.format(search))
        # store_history(search)
    return resp


app.run(host='0.0.0.0', port=5000)