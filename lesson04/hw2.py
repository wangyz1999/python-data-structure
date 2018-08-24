class DavidCai:
    def __init__(self, power=1, health=100):
        assert power > 0, "power must be positive"
        assert power <= 24, "Max power 24"
        assert health <= 100, "Max health 100"
        self.power = power
        self.health = health

    def __add__(self, other):
        return DavidCai(min(24, self.power + other.power),
                        min(100, self.health + other.health))

    def __mul__(self, other):
        return DavidCai(min(24, self.power * other.power),
                        min(100, self.health * other.health))

    def __str__(self):
        return "Power: {}\nHealth: {}".format(self.power, self.health)

    def __eq__(self, other):
        return self.power == other.power and self.health == other.health

if __name__ == "__main__":
    a = DavidCai(2, 9)
    b = DavidCai(2, 9)
    c = DavidCai(4, 5)
    print(a == b) #Ture
    print()
    print(str(a + c))
    print()
    print(str(a * b))
