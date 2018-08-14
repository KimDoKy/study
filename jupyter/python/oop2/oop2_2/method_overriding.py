class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print('{} can not do anything else'.format(self.name))

    # 나머지 메서드

class Car:
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    def drive(self):
        self.owner.concentrate()
        print('{} is driving now.'.format(self.owner.name))

    # 나머지 메서드

class SelfDrivingCar(Car):
    def drive(self):
        print('Car is driving by itself')

if __name__ == '__main__':
    car = Car('Greg')
    car.drive()
    print('')

    s_car = SelfDrivingCar('John')
    s_car.drive()
