from google.cloud import bigquery
from google.oauth2 import service_account
from sqlalchemy import create_engine


credentials = service_account.Credentials.from_service_account_file("CREDENTIALS.json")
client = bigquery.Client(credentials=credentials)

search = 'car'

query = f""" SELECT * FROM `ada-search-service.searchhistory_db.auctions` WHERE category = '{search}'"""

print(query)

df = client.query(query).to_dataframe()

print(df)
