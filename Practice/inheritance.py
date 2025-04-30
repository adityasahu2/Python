class Car:

    color = "Black"
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

    @classmethod
    def changeColor(cls, color):
        cls.color = color

    def changeColor2(self,color):
        self.__class__.color = color
    
    def changeColor3(self,color):
        Car.color = color #it change the class color not self color

class ToyotaCar(Car): #For multiple inheritance we can write ToyotaCar(Car,Bus,Truck)
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("Prius","electric")
print(car1.type)
print(car1.color)

car1.changeColor("Blue")
print(car1.color)

car1.changeColor2("Yellow")
print(car1.color)

car1.changeColor3("Green")
print(car1.color)

print(Car.color)