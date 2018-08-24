class Person:
    def __init__(self, name='David Cai'):
        self.name = name

    def setName(self, name):
        self.name = name

    def greet(self):
        print("Hello world! I'm {}".format(self.name))
