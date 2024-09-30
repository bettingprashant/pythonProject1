user_type = input("Enter the user type, admin, manager, guest\n")

match user_type:
    case "admin"  |  "manager":
        print("Hello Sir")
    case "guest":
        print("Hello, Guest")
    case _:
        print("Hello, There!")