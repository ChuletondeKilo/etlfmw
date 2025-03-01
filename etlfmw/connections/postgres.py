from ..interfaces import ConnectionI
import psycopg2
from psycopg2._psycopg import connection
from ..loggers import log_message

class ConnectionPostgre(ConnectionI):

    def __init__(self):
        self.connection: connection = None

    def connect(self):
        try:
            connection = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="Rotiman1*",
                host="localhost",
                port="5432"
            )
            self.connection = connection
        except Exception as e:
            print(f'Error connecting to Postgre: {e}')

    def disconnect(self) -> None:

        if self.connection:
            self.connection.close()
            print('Disconnecting from Postgre')

    def execute(self, query):

        try:
            cursor = self.connection.cursor()
            print(f'Executing query: {query}')
            cursor.execute(query)
            results = cursor.fetchall()
            self.connection.commit()
            return results
        except Exception as e:
            print(f'Error executing query: {e}')

    def load(self, data):

        ...