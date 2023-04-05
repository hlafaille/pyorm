from typing import List, Type
from pyorm.adapters import Adapter, SqliteAdapter
from pyorm.table import Table
from sqlite3 import Connection as sqlite_con


class Connection:
    """Represents a universal wrapper for a native Connection (ex: SQLite 'Connection' object)"""

    def __init__(self, native_connection) -> None:
        self.native_connection = native_connection


class Manager:
    """Handles communicating with the different adapters"""

    def __init__(self, adapter: Adapter) -> None:
        self.adapter = adapter

    def get_connection(self) -> Connection:
        """
        :returns: Connection instance from Adapter
        """
        con = Connection(native_connection=self.adapter.get_connection())
        return con

    def handle_table(self, table: Type[Table] | List[Type[Table]]) -> None:
        """
        Adds a table to the database if it doesn't already exist. The manager only gets a list of existing tables
        when the Manager is instantiated.
        :param table: Table instance
        """
