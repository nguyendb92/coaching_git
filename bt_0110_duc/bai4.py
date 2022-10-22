import random


class Weapon:
    def __init__(self, name, damage, attack_rating):
        self.name = name
        self.damage = damage
        self.attack_rating = attack_rating

    def __str__(self):
        return self.name


class Fighter:
    def __init__(self, name, hp, w):
        self.name = name
        self.HP = hp
        self.weapon = w

    def __str__(self):
        return f"{self.name}: HP {self.HP} / Weapon: {self.weapon}"

    def attack(self, someone):
        someone.HP -= self.weapon.damage * self.weapon.attack_rating

    def get_random_weapon(self, w):
        self.weapon = w
        # phat trien them de 2 dau si co the lay weapon luc runtime


sword = Weapon("kiem", 70, 3)
bow = Weapon("Cung", 50, 2)
gun = Weapon("Sung", 100, 5)
list_weapon = [sword, bow, gun]

duc = Fighter("Duc", 2000, random.choice(list_weapon))
viet = Fighter("Viet", 2000, random.choice(list_weapon))
print(duc)
print(viet)

players = [duc, viet]
first = random.choice(players)
second = [remain for remain in players if remain != first][0]

while first.HP > 0 and second.HP > 0:
    first.attack(second)
    second.attack(first)

print(first, second)
winner = None
if first.HP > second.HP:
    winner = first
elif first.HP < second.HP:
    winner = second

if winner:
    print("Winner: ", winner)
else:
    print("HOA")
