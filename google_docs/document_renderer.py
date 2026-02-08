from .document import Document

class DocumentRenderer:

    def render(self, document: Document) -> str:

        print("Rendering document...")
        rendered_elements = [element.render() for element in document.get_elements()]
        print("Document rendered successfully.")
        return "\n".join(rendered_elements)

