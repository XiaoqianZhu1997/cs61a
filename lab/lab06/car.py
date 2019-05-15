class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.make + ' ' + self.model + ' cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return self.make + ' ' + self.model + ' gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)

hilfingers_car = Car('Tesla', 'Model S')
print(Car.size)
print(hilfingers_car.color)
hilfingers_car.paint('black')
print(hilfingers_car.color)
Car.paint(hilfingers_car, 'black')
print(hilfingers_car.color)

hilfingers_truck = MonsterTruck('Monster Truck', 'XXL')
print(hilfingers_car.size)
print(hilfingers_truck.size)



class FoodTruck(MonsterTruck):
    delicious = 'meh'
    def serve(self):
        if FoodTruck.size == 'delicious':
            print('Yum!')
        if self.food != 'Tacos':
            return 'But no tacos...'
        else:
            return 'Mmm!'

taco_truck = FoodTruck('Tacos', 'Truck')
print(FoodTruck.pop_tire(taco_truck))