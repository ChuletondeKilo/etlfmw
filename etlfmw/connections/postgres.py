from ..interfaces import ConnectionI
import psycopg2
from psycopg2._psycopg import connection as postgreconn, cursor as postgrecursor
from psycopg2.errors import OperationalError
from ..connections.schema import PostgresConnectionSchema, ConnectionSchema

class ConnectionPostgre(ConnectionI):

    __slots__ = ['metadata', '_params', 'recon_info', 'connection', 'cursor']

    def __init__(self, connection: ConnectionSchema):

        self.metadata: dict = {k: v for k, v in connection.__dict__.items() if k not in ('params','recon_info')}
        self._connparams: PostgresConnectionSchema = connection["params"]
        self.recon_info: dict = getattr(connection, "recon_info", None)
        self.connection: postgreconn = None
        self.cursor: postgrecursor = None

    def connect(self):

        try:

            self.connection = psycopg2.connect(
                **self._connparams
            )

        except OperationalError as e:

            print(f'Error connecting to Postgre: {e}.')
            print(f'Proceeding to disconnect')

            self.disconnect()

            print(f'Error connecting to Postgre: {e}')

    def disconnect(self) -> None:

        if self.connection or self.cursor:

            print('Closing Postre cursor and connection.')

            try:

                if self.connection:

                    self.connection.close()
            
            except Exception as e:

                print(f'Encountered Error {e} while trying to close connection.')
    
    def reconnect(self):

        if self.recon_info:

            print('Reconnecting to Postgre.')

            for _ in self.recon_info['retries']:

                self.connect()

                if self.connection:

                    break

    def execute(self, query):

        try:

            print(f'Executing query: {query}')
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.connection.commit()

            return results

        except Exception as e:

            print(f'Error executing query: {e}')

    def load(self, data):

        ...