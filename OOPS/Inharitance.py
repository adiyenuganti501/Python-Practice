class Car:
    def __init__(self,name,brand,year):
        self.name=name
        self.brand=brand
        self.year=year
    def showdetals(self):
        print(f"Details are {self.name} {self.brand} and {self.year}")
class Audi(Car):
    def __init__(self,name,brand,year,color):
        super().__init__(name,brand,year)
        self.color=color
    def showColor(self):
        print("Color is", self.color)

a=Audi("Audi","501",2026,"Grey")
a.showdetals()
a.showColor()