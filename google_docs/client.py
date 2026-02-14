from google_docs.document import Document
from google_docs.document_renderer import DocumentRenderer
from google_docs.persistance import SaveToFile
from google_docs.document_editor import DocumentEditor

def main():
    # Create core objects
    document = Document()
    storage = SaveToFile()  # Switch to DBStorage without changing editor
    editor = DocumentEditor(document, storage)
    renderer = DocumentRenderer()

    # Editing
    editor.add_text("Hello, world!")
    editor.add_image("/images/design.png")
    editor.add_text("This is a Google Docs LLD example.")

    # Rendering
    renderer.render(document)

    # Persistence
    editor.save()


if __name__ == "__main__":
    main()
