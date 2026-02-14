from abc import ABC, abstractmethod

class Persistence(ABC):
    @abstractmethod
    def save(self, document) -> str:
        pass

class SaveToFile(Persistence):
    def save(self, document) -> str:
        print("Saving document to file...")
        return "Document saved to file successfully."

class SaveToDatabase(Persistence):
    def save(self, document) -> str:
        print("Saving document to database...")
        return "Document saved to database successfully."
