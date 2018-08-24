class AssassinNode:
    def __init__(self, name, target=None):
        self.name = name
        self.killer = None
        self.target = target


class KillRing:
    def __init__(self, names):
        self.head = AssassinNode(names[0])
        player = self.head
        for name in names[1:]:
            nextPlayer = AssassinNode(name)
            player.target = nextPlayer
            player = player.target
        player.target = self.head


class Graveyard:
    def __init__(self):
        self.head = None
        self.tail = self.head


class AssassinManager:
    def __init__(self, names):
        self.ring = KillRing(names)
        self.grave = Graveyard()

    def printKillRing(self):
        print("Current kill ring:")
        node = self.ring.head
        print("{:>9} is stalking {}".format(node.name, node.target.name))
        while node.target is not self.ring.head:
            node = node.target
            print("{:>9} is stalking {}".format(node.name, node.target.name))

    def printGraveyard(self):
        node = self.grave.head
        while node is not None:
            print("{:>9} was killed by {}".format(node.name, node.killer.name))
            node = node.target

    def kill(self, name):
        node = self.ring.head
        while node.target.name.lower() != name.lower():
            node = node.target
        if node.target.name.lower() == self.ring.head.name.lower():
            self.ring.head = self.ring.head.target
        node.target.killer = node
        dead_node = node.target
        node.target = node.target.target
        if self.grave.head is None:
            self.grave.head = dead_node
        else:
            self.grave.tail.target = dead_node
        self.grave.tail = dead_node
        dead_node.target = None

    def killRingContains(self, name):
        node = self.ring.head
        while True:
            if node.name.lower() == name.lower():
                return True
            if node.target is self.ring.head:
                break
            node = node.target
        return False

    def graveyardContains(self, name):
        node = self.grave.head
        while node .target is not None:
            if node.name.lower() == name.lower():
                return True
            node = node.target
        return False

    def gameOver(self):
        return self.ring.head.target is self.ring.head

    def winner(self):
        if self.gameOver():
            return self.ring.head.name
        return None


def AssassinMain():
    nameList = ['David Cai', 'Thanos', 'Jason', 'Bishi']
    game = AssassinManager(nameList)
    while game.winner() is None:
        game.printKillRing()
        print("\nCurrent Graveyard:")
        game.printGraveyard()
        print()
        while True:
            victim = input("next victim? ")
            print()
            if game.killRingContains(victim):
                game.kill(victim)
                break
            print("Player not found in Kill Ring")

    print("Game was won by {}".format(game.winner()))
    print("\nFinal graveyard is as follows:")
    game.printGraveyard()


if __name__ == "__main__":
    AssassinMain()
