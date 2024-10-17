user_age = int(input("Enter your age\n"))
print(type(user_age))

if user_age>=18:
    print(f"He can go to club ->{user_age}")
else:
    print(f"can't go to club ->{user_age}")
