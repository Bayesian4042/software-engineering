class IMultiFunctionDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass


class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing")


class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning")


class Fax(IMultiFunctionDevice):
    def fax(self):
        print("Faxing")
