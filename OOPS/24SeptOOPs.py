class vehical:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def showDeatils(self):
        print(f"Vehical details are {self.name} and {self.color}")

class car(vehical):
    def __init__(self,name,color,year):
        super().__init__(name,color)
        self.year=year
    def showYear(self):
        print(f"Deatils are {self.year}")
a=car("Car","Black",2025)
a.showDeatils()
a.showYear()