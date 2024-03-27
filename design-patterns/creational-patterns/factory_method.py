"""
Define an interface for creating an object, but let subclasses decide which class to instantiate. 
Factory Method lets a class defer instantiation to subclasses.

When to use:
When a caller can't anticipate the types of objects it must create.
When you have many objects of common type. 

Two variants:
1. Parameterized Factory Method
2. Classic GoF
"""

# Document Management System
class Document:
    def __init__(self, name):
        self.name = name
    
    def open(self):
        pass

    def save(self):
        pass

class PdfDocument(Document):
    def open(self):
        print("Opening PDF document")

    def save(self):
        print("Saving PDF document")

class WordDocument(Document):
    def open(self):
        print("Opening Word document")

    def save(self):
        print("Saving Word document")

# Document creator
class DocumentCreator:
    def create_document(self, type):
        if type == "pdf":
            return PdfDocument("pdf")
        elif type == "word":
            return WordDocument("word")

if __name__ == "__main__":
    creator = DocumentCreator()
    pdf = creator.create_document("pdf")
    pdf.open()
    pdf.save()

    word = creator.create_document("word")
    word.open()
    word.save()


