class Bird:
    def fly(self):
        pass

def FlyingBird(Bird):
    def fly(self):
        print("Bird flying")


def NonFlyingBird(Bird):
    def fly(self):
        raise AttributeError("Penguins can't fly")

def Penguin(NonFlyingBird):
    pass