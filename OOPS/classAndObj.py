class Human:
    def __init__(self,name,age,city,gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
h1=Human("Adi",30,"hyd","male")
print(f"{h1.name} {h1.age} {h1.city} {h1.gender}")
h2=Human("Friya",25,"hyd","female")
print(f"{h2.name} {h2.age} {h2.city} {h2.gender}")
