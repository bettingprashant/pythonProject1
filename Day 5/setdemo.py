#1
# myset={"apple", "banana", "Cherry"}
# print(myset)

#2
# myset={"apple", "banana", "Cherry"}
# for i in myset:
#     print(i)


# myset={"apple", "banana", "Cherry"}
# if "apple" in myset:
#     print("Yes")
# else:
#     print("No")
#3
# myset={"apple", "banana", "Cherry"}
# print("banana" in myset)
# print("banana2" in myset)

#4
# myset={"apple", "banana", "Cherry"}
# myset.add("Lichi")
# print(myset)

#5.1
# myset={"apple", "banana", "Cherry"}
# myset.update(["mango","Orange"])
# print(myset)

#5.2
# myset={"apple", "banana", "Cherry"}
# print(len(myset))

#6
# myset={"apple", "banana", "Cherry"}
# myset.remove("banana")
# print(myset)
# # myset.remove("xyz")
# myset.discard("apple")
# myset.discard("xyz")
# print(myset)

#7
# myset={"apple", "banana", "Cherry"}
# # myset.clear()
# del myset  #NameError: name 'myset' is not defined
# print(myset)

#8
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

