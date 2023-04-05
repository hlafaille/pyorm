from sqlite3 import Connection

from pyorm.statements import Statement


class Adapter:
    def get_connection(self):
        """
        :returns: Native connection object
        """

    def prepare_statement(self, statement: Statement) -> str:
        """
        Prepares an SQL Statement
        :param statement: Statement objectS
        """


class SqliteAdapter(Adapter):
    def __init__(self, path: str) -> None:
        """
        Using the stdlib sqlite module, this adapter will translate declarative py-orm code into sqlite compatible SQL.
        This adapter does NOT support async.
        """
        self._path = path

    def get_connection(self) -> Connection:
        """
        :returns: Native SQLite connection object
        """
        con = Connection(database=self._path)
        return con

    def prepare_statement(self, statement: Statement) -> str:
        """
        Prepares a native SQLite statement
        :param statement: Statement string
        """
