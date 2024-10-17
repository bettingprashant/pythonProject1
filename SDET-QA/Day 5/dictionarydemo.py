#1

# mydic={100:"x",101:"y",102:"z"}
# print(mydic)

#2

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2022
# }
# print(mydic["brand"])
# x=mydic.get("brand")
# print(x)

#3
# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
# print(mydic)
# mydic["brand"]="Honda"
# print(mydic)

#4

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
# for i in mydic:
#     print(i)
#
# for i in mydic:
#     print(mydic[i])
#
# for i in mydic.values():
#     print(i)
#
# for x,y in mydic.items():
#     print(x,y)

#5

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
#
# # if "model" in mydic:
# #     print("exist")
# # else:
# #     print("not exist")
#
# print("model" in mydic)

#6

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
# print(len(mydic))

#7

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
#
# mydic["color"]="Red"
# print(mydic)

#9

# mydic={
# "brand": "Hyundai",
# "model": "Verna",
# "year": 2023
# }
# # mydic.pop("year")
# # print(mydic)
#
# # del mydic["year"]
# # print(mydic)
#
# # del mydic
# # print(mydic) #NameError: name 'mydic' is not defined
#
# mydic.clear()
# print(mydic)

#9

mydic1={
"brand": "Hyundai",
"model": "Verna",
"year": 2023
}

# mydic2=mydic1
# print(mydic2)

mydic2=mydic1.copy()
print(mydic2)