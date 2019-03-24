class Animal():

    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("Animal Eat")

    def in_which(self):
        print("In Animal")

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self) #Can b intialized
        print("Dog Created")

    def eat(self):
        print("Dog Eating") #OverWriting

    def bark(self):
        print("Wooof")

dog = Dog()
dog.eat()
dog.in_which()
dog.bark()
