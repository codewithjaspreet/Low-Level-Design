
# DIP - Dependency Inversion Principle
# High Level Modules should not  depend on low level module but rather should depend on abstraction layer that controls other low level modules

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MongoDB(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")


class PostgresDB(Database):
    def save(self, data):
        print(f"Saving {data} to PostgresDB")

class Application:
    def __init__(self, database: Database):
        self.database = database

    def persist(self, data):
        self.database.save(data)


mongo_app = Application(MongoDB())
mongo_app.persist("User Data")

postgres_app = Application(PostgresDB())
postgres_app.persist("Order Data")
