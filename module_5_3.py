class Building:

    def __init__(self, number, type_):
        self.numberOfFloors = number
        self.buildingType = type_
        # print(self)
        # print(self.buildingType)

    def construction_of_floors(self):
        self.numberOfFloors += 1
        print(f'теперь у {self} {self.numberOfFloors} этажей')

    def __str__(self):
        return f'{self.buildingType}'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(1, "Hata")
h2 = Building(1, "Hata")
print("eqality_1: ", h1 == h2)

sk_1 = Building(77, 'skyskraper')
sk_2 = Building(77, 'skyskraper')
sk_2.construction_of_floors()
print("eqality_2: ", sk_1 == sk_2)