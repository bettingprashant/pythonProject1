class VMOLoginPage:
    def __init__(self,email_arg, paswword_arg):
        self.email = email_arg
        self.password = paswword_arg

    def login_confirm(self):
        if self.email == "Pramod@gmail.com" and self.password =="Test@123":
            print("Allowed to login")
        else:
            print("Not allowed")

email = input("Enter the email \n")
password = input("Enter the Password \n")

vwo_obj = VMOLoginPage(email,password)
vwo_obj.login_confirm()

pramod = VMOLoginPage("Pramod@gmail.com","Test@123")
pramod.login_confirm()