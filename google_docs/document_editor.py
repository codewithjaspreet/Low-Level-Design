from .database import Database
from .document import Document
from .document_element import TextElement, ImageElement
from .persistance import Persistence
class DocumentEditor:
    """
    Handles editing operations.
    Depends only on abstractions.
    """

    def __init__(self, document: Document, storage: Persistence):
        self.document = document
        self.storage = storage

    def add_text(self, text: str) -> None:
        self.document.add_element(TextElement(text))

    def add_image(self, image_path: str) -> None:
        self.document.add_element(ImageElement(image_path))

    def save(self) -> None:
        serialized_data = self._serialize_document()
        self.storage.save(serialized_data)

    def _serialize_document(self) -> str:
        return "\n".join(
            element.render() for element in self.document.get_elements()
        )
