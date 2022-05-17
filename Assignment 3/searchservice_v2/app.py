from flask import Flask, json , request, Response
import requests
from google.cloud import bigquery

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/searchservice/<search>', methods=['GET'])
def read_data(search):
    fake_db = {"1":['Car_1', 'Car_2','Car_3'], "1":['Laptop_1', 'Laptop_2']}
    # from google.cloud import bigquery
    # from google.oauth2 import service_account
    # from sqlalchemy import create_engine

    # credentials = service_account.Credentials.from_service_account_file("CREDENTIALS.json")
    # client = bigquery.Client(credentials=credentials)

    # The search history should be connected to the account domain, history is stored for you account
    # if search == 'history':
    #     query = f""" SELECT * FROM `ada-search-service.searchhistory_db.search_history`"""
    # # This query should query the auction database not the current placeholder 
    # else:
    #     query = f""" SELECT * FROM `ada-search-service.searchhistory_db.auctions` WHERE category = '{search}'"""


    # df = client.query(query).to_dataframe()

    # if len(df) >= 1:
    #     resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    #     if search != 'history':
    #         requests.post('https://us-central1-ada-search-service.cloudfunctions.net/update_history', json={"search":search})
    # else:
    # resp = json.dumps({'message': 'No data found for search term: {}'.format(search)}, sort_keys=False, indent=4), 200    
    
    resp = fake_db[search]
    return resp


app.run(host='0.0.0.0', port=5000)