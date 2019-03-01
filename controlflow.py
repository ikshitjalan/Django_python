mypairs = [(1,2),(3,4),(5,6)]
for (tup1,tup2) in mypairs:
    print(tup2)
    print(tup1)
    print(tup2)

mylist = list(range(0,21,2))
print(mylist)

# List Comprehension

x = [1,2,3,4,5]

out = [num**2 for num in x]
print(out)
