a = 10

class Myclass:

    public_var = "I am PUBLIC"
    __balance = 100

    __private_var = "I am PRIVATE"
    __password = "1234"
    _protected_var = "I am protected"

object = Myclass()
print(object.public_var)
print(object._protected_var)
print(object.__balance)