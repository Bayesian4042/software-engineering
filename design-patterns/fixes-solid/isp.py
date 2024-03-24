class IPrinter:
    def print(self, document):
        pass

class IScanner:
    def scan(self, document):
        pass

class IFax:
    def fax(self, document):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing")