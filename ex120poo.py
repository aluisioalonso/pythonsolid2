class Vehicle:
    color = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

veiculo = Bus('school', 180, 12)
print(f'color: {veiculo.color}, vehicle name: {veiculo.name}, Speed: {veiculo.max_speed}, Mileage: {veiculo.name}')

