class Dog():

    species = "All are kuttas"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name



dog = Dog("Lab","softy")
otherdog = Dog(breed= "huskie",name="kutta")
print(dog.breed)
print(otherdog.breed)
print(dog.name)
print(dog.species)


class Circle():

    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area (self):
        return self.radius*self.radius*Circle.pi

    def set_radius (self,new_r):
        self.radius = new_r


cir = Circle(3)
print(cir.radius)
print(cir.area())
