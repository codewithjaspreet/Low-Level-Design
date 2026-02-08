from .persistance import Persistance

class Database(Persistance):
    def save(self, document) -> str:
        print("Saving document to database...")
        return "Document saved to database successfully."
