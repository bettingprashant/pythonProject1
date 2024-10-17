# mylist1=["10,20,30,40"]
# mylist2=["apple","banana","cherry"]
# mylist3=["aaple",10, "banana",20]
# mylist=list()
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

# mylist=("apple","cherry","banana")
# print(mylist[0])
# print(mylist[2])


# mylist=("apple","cherry","banana","mango","coconut","litchi","guava")
# print(mylist[2:5])
# print(mylist[-4:-1])

# mylist=("apple","cherry","banana")
# print(mylist)
# mylist[0]="orange"
# print(mylist) ['orange','banana','cherry']


# mylist=("apple","cherry","banana")
# for i in mylist:
#     print(i)

# mylist=("apple","cherry","banana")
# if "apple" in mylist:
#     print("apple is available")
# else:
#     print("apple is not available")

# mylist = ["apple", "banana", "orange"]
# print(len(mylist))


# mylist = ["apple", "banana", "orange"]
# # mylist.append("cherry")
# mylist.insert(1,"Cherry")
# print(mylist)


# mylist = ["apple", "banana", "orange"]
# # mylist.pop(0)
# # del mylist[0]
# mylist.clear()
# print(mylist)



# mylist1 = ["apple", "banana", "orange"]
# # mylist2 = list(mylist1)
# mylist2= mylist1.copy()
# print(mylist1)
# print(mylist2)


# list1=("a", "b", "c")
# list2=(1,2,3)
# list3=(list1+list2)
# print(list3)

# list1=["a", "b", "c"]
# list2=[1,2,3]
#
# for i in list2:
#     list1.append(i)
# print(list1)

# list1=["a", "b", "c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)

#list Comparison
mylist1=[10,20,30]
mylist2=[10,20,30]

if mylist1==mylist2:
    print("Eqaul")
else:
    print("not equal")