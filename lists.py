mylist = ['ikshit',1,4,4.0,False,'jalan']
print((mylist[:3]))
mylist[0] = 'New Item'
mylist.append(['x','y','z'])
mylist.extend(['x','y','z'])
print(mylist)
item = mylist.pop(0)
print(item)
print(mylist)
mylist.reverse()
print(mylist)

#nested List

mylist = [1,2,['x','y','z']]

print(mylist[2][1])

matrix = [[1,2,3,],[4,5,6,],[7,8,9]]
first_column = [row[0] for row in matrix]
print(first_column)
