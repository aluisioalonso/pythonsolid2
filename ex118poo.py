class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

veiculo = Bus('school', 180, 12)
print(f'vehicle name: {veiculo.name}, Speed: {veiculo.max_speed}, Mileage: {veiculo.name}')