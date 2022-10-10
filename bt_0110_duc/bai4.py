import random


class Weapon:
    def __init__(self, damage, attack_rating):
        self.damage = damage
        self.attack_rating = attack_rating


class Player(Weapon):
    HP = 1000
    # def __init__(self, damage, attack_rating):
    #     super().__init__(damage, attack_rating)

    def __init__(self, weapon):
        self.damage = weapon.damage
        self.attack_rating = weapon.attack_rating


sword = Weapon(16, 2)
bow = Weapon(14, 2)
gun = Weapon(20, 2)
list_weapon = [sword, bow, gun]

player1 = Player(random.choice(list_weapon))
player2 = Player(random.choice(list_weapon))

while player1.HP > 0 and player2.HP > 0:
    player1.HP -= player2.damage * player2.attack_rating
    player2.HP -= player1.damage * player1.attack_rating


if player1.HP == 0:
    print("Player2 win")
    print(player2.HP)
    print(player1.HP)

elif player2.HP == 0:
    print("Player1 win")
    print(player2.HP)
    print(player1.HP)

else:
    print("Tie")
