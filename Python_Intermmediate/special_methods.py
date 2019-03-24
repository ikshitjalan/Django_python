class Book():

    def __init__(self,title,pages,author):
        self.title = title
        self.pages = pages
        self.author = author

    def __str__(self): #Used for string representation of objects
        return "Title: {}, Pages : {}, Author: {}".format(self.title,self.pages,self.author)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is now Destroyed")

b = Book("pkmkb",369,"ikshit")

print(b)
print(len(b))

del b
print(b.title)
