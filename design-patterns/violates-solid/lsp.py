class Bird:
    def fly(self):
        print("Bird flying")


class Penguin(Bird):
    def fly(self):
        raise AttributeError("Penguins can't fly")