class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter only int value of a")
        else:
            print(a)
        finally:
            print("FInally Anyhow I will be printed")

x = XYZ()
x.f1()