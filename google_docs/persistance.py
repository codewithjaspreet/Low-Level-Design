from abc import ABC, abstractmethod

class Persistance(ABC):
    @abstractmethod
    def save(self, document) -> str :
        pass

class SavetoFile(Persistance):
    def save(self, document) -> str:
        print("Saving document to file...")
        return "Document saved to file successfully."

class SaveToDatabase(Persistance):
    def save(self, document) -> str:
        print("Saving document to database...")
        return "Document saved to database successfully."
