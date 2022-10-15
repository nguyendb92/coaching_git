class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"


class Bus(Vehicle):
    pass


p1 = Vehicle("School Volvo", 180, 12)
print(p1)
