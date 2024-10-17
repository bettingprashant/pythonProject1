#Dictionary
# student_information = dict(name = "Pramod", age = "67", address = "KA")
student_information = {
    "name" : "Pramod",
    # "age" : 65,
    "age" : 67,
    "address" : {
        "home_address" : "ND",
        "office_address" : "KA"
    }
}
print(student_information)
print(student_information["name"])
print(student_information["age"])
print(student_information["address"])

student_information["age"] = 100
print(student_information)