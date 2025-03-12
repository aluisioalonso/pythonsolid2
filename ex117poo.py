class Veiculo:
    def __init__(self, max_speed= 100, mileage=0):
        self.mileage = mileage
        self.max_speed = max_speed

    def display_info(self):
        print(f'velocidade maxima: {self.max_speed} km/h')
        print(f'quilometragem: {self.mileage} km')


veiculo1 = Veiculo(200, 1550)
veiculo1.display_info()