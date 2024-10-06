my_list = [1,2,3]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[2])

my_list[0] = "Raj"
my_list[1] = "Singh"
my_list[2] = "Singh"

print("element of index 0 - ", my_list[0])
print("element of index 0 - ", my_list[1])
print("element of index 0 - ", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1,10):
    print(i)


print("_ ____________")
my_list = [1,2,3]

# Append

my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list)

my_list.extend([7,8,9])
my_list.extend([10,"Raj"])
print(my_list)

my_list.insert(1,"Singh")
print(my_list)

# my_list[0] = 1  # replace
# print(my_list)

#remove

my_list.remove("Singh")
print(my_list)

print("----------------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Raj")
my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)