from random import randint, uniform


class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.HP = randint(1000, 1500)
        self.weapon = Weapon(weapon)

    def attacks(self, other_player):
        print("{} attacks {}".format(self.name, other_player.name))
        self.weapon.use_on(other_player)

    def injure(self, dmg):
        print("{} suffers {} dmg".format(self.name, dmg))
        self.HP -= dmg
        print("{} has {} HP remaining.".format(self.name, self.HP))
        if self.HP <= 0:
            print("{} Loser...".format(self.name))
            raise Loser


class Weapon:
    weapons = {
        "Crystal Sword": {"dmg": 75, "accuracy": 50},
        "Hunter Bow": {"dmg": 80, "accuracy": 100},
    }

    def __init__(self, weapon):
        weapon = weapon.lower().strip()
        if weapon in self.weapons:
            self.name = self.weapons[weapon]
            self.dmg = self.name["dmg"]
            self.accuracy = self.name["accuracry"]

    def use_on(self, opponent):
        # Sử dụng phân phối xác suất thống nhất và xác suất chính xác có
        # trọng số của vũ khí để quyết định xem vũ khí có bắn trúng đối thủ hay không
        if (randint(0, self.accuracy) / 100) > uniform(0, 1):
            opponent.injure(self.dmg)
        else:
            print("Missed!")


class Loser(Exception):
    pass


if __name__ == "__main__":
    Player1 = Player("Doppelganger", "Crystal Sword")
    Player2 = Player("Warrior", "Hunter Bow")

    no_one_loser = True
    print("Doppelganger and Warrior want to fight!")
    while no_one_loser:
        try:
            print("Next")
            Player1.attacks(Player2)
            print("Next")
            Player2.attacks(Player1)
        except Loser:
            no_one_loser = False
            print("The battle's done!")
