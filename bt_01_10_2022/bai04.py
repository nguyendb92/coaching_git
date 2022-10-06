class Player:
    def __init__(self, name1, hp1, name2, hp2):
        self.name1 = name1
        self.name2 = name2
        self.hp1 = hp1
        self.hp2 = hp2


class Weapon:
    def __init__(self, damage1, damage2):
        self.damage1 = damage1
        self.damage2 = damage2


class Result(Player, Weapon):
    def test(self):
        while (self.hp1 > 0) and (self.hp2 > 0):
            self.hp1 -= self.damage2
            self.hp2 -= self.damage1
        print(self.name1, self.hp1)
        print(self.name2, self.hp2)


p1 = Result("viet", 1000, "duc", 1000, 300, 200)
p1.test()