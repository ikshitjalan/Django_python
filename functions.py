def hello_() :
    return 'Hello'

result = hello_()
print(result)

def hello():
    print('Hello')

hello()

def add_num(num1,num2):
    return (num1+num2)

result =add_num(2,5)
print(result)

result = add_num('2','5')
print(result,type(result))

# Filter Function

list1 = list(range(0,11))

def even(num):
    return num%2==0

evens = filter(even,list1)
print(list(evens))

# Lambda Function

evens2 = filter(lambda num:num%2==0,list1)
print(list(evens2))
