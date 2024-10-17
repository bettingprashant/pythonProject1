#1
# mytuple = ("mango", "banana", "Cherry")
# print(mytuple)

#2
# mytuple = ("mango", "banana", "Cherry")
# print(mytuple[1])
# print(mytuple[-1])

#3
# mytuple = ("mango", "banana", "Cherry", "Orange", "Guava", "Watermelon")
# print (mytuple[2:5])
# print (mytuple[-4:-1])

#4
# mytuple = ("mango", "banana", "Cherry")
# mytuple = ("apple", 100, 200)
# mylist=list(mytuple)
# mylist[0] = "Orange"
# mytuple=tuple(mylist)
# print(mytuple)
# print(mytuple)

#5
# mytuple = ("apple", "banana", "orange")
# for i in mytuple:
#     print(i)

#6
# mytuple = ("apple", "banana", "orange")
# if "banana1" in mytuple:
#     print("yes")
# else:
#     print("no")

#7
# mytuple = ("apple", "banana", "orange")
# print(len(mytuple))

#8
# mytuple = ("apple", "banana", "orange")
# mytuple[0] = "orange" # TypeError: 'tuple' object does not support item assignment
# print(mytuple)

#9
# mytuple1 = ("apple", "banana", "orange")
# mytuple2 = mytuple1
# print(mytuple2)

#10
# mytuple = ("apple", "banana", "orange")
# # mytuple.remove("apple")
# del mytuple
# print(mytuple)

#11
# tuple1=(10,20,30)
# tuple2=('a','b','c')
#
# tuple3= tuple1+tuple2
# print(tuple3)

#12 Tuples Comparison
tuple1=(10,20,30)
tuple2=('a','b','c')

if tuple1==tuple2:
    print("equal")
else:
    print("Not Equal")