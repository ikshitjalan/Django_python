def hello(name= "ikshit"):
    print("Hello function has been called")
    def greet():
        return ("String is inside greet")
    def welcome():
        return ("String is inside welcome")

    if (name=="ikshit"):
        return greet
    else:
        return welcome
x = hello()
print(x())


def name():
    return ("ikshit")

def other(func):
    print('Hoi')
    print(func())

other(name)


def new_decorator(func):
    print("Code before exe")
    def wrap_func():
        func()
        print("function has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Func needs a decorator")

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
