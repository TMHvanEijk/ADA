from flask import Flask, json , request, Response
import requests
from google.cloud import bigquery

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
    client = bigquery.Client()

    query = (f'SELECT * from "ada-search-service.searchhistory_db.search_history" WHERE category = {search}')
    job_config = bigquery.QueryJobConfig(use_legacy_sql=True)
    query_job = client.query(query, job_config=job_config)
    
    # return json.dumps({'type of search': '{}'.format(type(search))})
    if search == 'history':
        df = db_util.read_data_records('history_db', search)
        resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    else:
        requests.post('https://us-central1-ada-search-service.cloudfunctions.net/update_history', json={"search":search})
        df = db_util.read_data_records('search_db', search)
        resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
        # requests.post(f'https://us-central1-ada-search-service.cloudfunctions.net/update_history?search={search}')
        # store_history(search)
    return resp


app.run(host='0.0.0.0', port=5000)