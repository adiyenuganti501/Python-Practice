class Car:
    def __init__(self,name,brand,year):
        self.name=name
        self.brand=brand
        self.year=year
    def showdetals(self):
        print(f"Details are {self.name} {self.brand} and {self.year}")
class Audi(Car):
    pass

a=Audi("Audi","501",2026)
a.showdetals()