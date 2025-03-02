from ..interfaces import ConnectionI
import psycopg2
from psycopg2._psycopg import connection as postgreconn
from ..connections.schema import PostgresConnectionSchema, ConnectionSchema
from ..loggers import log_message

class ConnectionPostgre(ConnectionI):

    __slots__ = ['metadata', '_params']

    def __init__(self, connection: ConnectionSchema):

        self.metadata: dict = {k: v for k, v in connection.__dict__.items() if k != 'params'}
        self._connparams: PostgresConnectionSchema = connection["params"]
        self.connection: postgreconn = None

    def connect(self):
        try:
            connection = psycopg2.connect(
                **self._connparams
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