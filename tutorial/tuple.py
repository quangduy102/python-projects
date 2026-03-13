#operation with tuple
#different between list and tuple is that tuple is immutable, we cannot change the value of tuple after it is created

coordinates = (1,2) 

#tuple is immutable, we cannot change the value of tuple after it is created
print(coordinates[0])

#if I try to change the value of tuple, it will raise an error

#combine two tuple
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print( tuple1 + tuple2)

#add tuple to list
list1 = [1,2,3]
tuple3 = (4,5,6)
list1.append(tuple3)
print(list1)

