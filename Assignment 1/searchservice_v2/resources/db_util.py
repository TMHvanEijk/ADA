import os

import pandas as pd
import sqlalchemy as db
from sqlalchemy import Column, Float, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from google.cloud import storage


class DBUtil:

    def __init__(self):
        # The database URL is provided as an env. variable
        if 'DB_URL' in os.environ:
            db_url = os.environ['DB_URL']
        else:
            db_url = 'sqlite:///search.db'
        # create the database
        self.engine = db.create_engine(db_url, echo=True)
        self._reflect()

    def create_tb(self, table_name, column_names):
        # Get a connection to the database
        conn = self.engine.connect()
        self._reflect()
        # Start the database transaction
        trans = conn.begin()
        # Define the columns of the table. Assume that a list of column names are provided and column type is float.
        columns = (Column(name, String, quote=False) for name in column_names)
        v_table = Table(table_name, self.Base.metadata,
                        extend_existing=True, *columns)
        v_table.create(self.engine, checkfirst=True)
        # End the database transaction
        trans.commit()

    def drop_tb(self, table_name):
        conn = self.engine.connect()
        trans = conn.begin()
        self._reflect()
        # get a reference to the table
        v_table = self.Base.metadata.tables[table_name]
        v_table.drop(self.engine, checkfirst=True)
        trans.commit()

    def add_data_records(self, table_name, records):
        self._reflect()
        # get a reference to the table
        v_table = self.Base.metadata.tables[table_name]
        # get a query object for inserting data
        query = db.insert(v_table)
        connection = self.engine.connect()
        trans = connection.begin()
        # run the query
        connection.execute(query, records)
        trans.commit()

    def read_data_records(self, table_name, category):
        self._reflect()
        v_table = self.Base.metadata.tables[table_name]
        connection = self.engine.connect()
        # if category != 1:
        #     query = f"SELECT * FROM {table_name} WHERE category={category}"
        # else:
        #     query = f"SELECT * FROM {table_name}"
        trans = connection.begin()
        # get a query object for reading all data
        if category == 'history':
            query = db.select([v_table])
        else:
            query = db.select([v_table]).where(v_table.columns.category == category)
        # read all data
        df = pd.read_sql_query(query, con=connection)
        trans.commit()
        return df

    # refresh meta-data
    def _reflect(self):
        self.Base = declarative_base()
        self.Base.metadata.reflect(self.engine)