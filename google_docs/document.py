from typing import List
from .document_element import DocumentElement

class Document():


    def __init__(self):
        self._elements = List[DocumentElement] = []


    def add_elemennt(self, element: DocumentElement):
        self._elements.append(element)

    def get_elements(self) -> List[DocumentElement]:
        return self._elements
