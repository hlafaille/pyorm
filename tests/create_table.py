from pyorm.adapters import SqliteAdapter
from pyorm.manager import Manager
from pyorm.table import Table


class Customers(Table):
    # define table specifics at the top, always!
    tablename = "customers"
    comment = "Our lovely paying customers"

    # begin defining your columns here. note: if the column name is 'id_', the trailing '_' will be removed!
    id_: int
    name: str


if __name__ == "__main__":
    # before creating your 'app' instance (ex: FastAPI/Flask), create a 'Manager' instance with your database as the 'adapter'
    manager = Manager(
        adapter=SqliteAdapter(
            path="test.db"
        )
    )

    # now, tell the manager about your tables
    manager.handle_table(Customers)

    print(Customers.__dict__)
