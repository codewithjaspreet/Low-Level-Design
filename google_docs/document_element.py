from abc import ABC, abstractmethod


class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        """Render the document element as a string."""
        ...


class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class ImageElement(DocumentElement):
    def __init__(self, image_path):
        self.image_path = image_path

    def render(self):
        return f"<img src='{self.image_path}' />"
