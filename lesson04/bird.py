class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaaaah... Eat David Cai")
            self.hungry = False

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "Squawk! David Cai no yummy"

    def sing(self):
        print(self.sound)
