from flask import Flask, json , request, Response
import requests
from google.cloud import bigquery

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/searchservice/<search>', methods=['GET'])
def read_data(search):
    from google.cloud import bigquery
    from google.oauth2 import service_account
    from sqlalchemy import create_engine

    credentials = service_account.Credentials.from_service_account_file("CREDENTIALS.json")
    client = bigquery.Client(credentials=credentials)

    if search == 'history':
        query = f""" SELECT * FROM `ada-search-service.searchhistory_db.search_history`"""
    else:
        query = f""" SELECT * FROM `ada-search-service.searchhistory_db.auctions` WHERE category = '{search}'"""
        requests.post('https://us-central1-ada-search-service.cloudfunctions.net/update_history', json={"search":search})


    df = client.query(query).to_dataframe()

    if len(df) >= 1:
        resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    else:
        resp = json.dumps({'message': 'No data found for search_term: {}'.format(search)}, sort_keys=False, indent=4), 200

    return resp


app.run(host='0.0.0.0', port=5000)