# Multilevel Inheritance

class GrandFather:
    gold = "2 Kg"
    def bhk1(self):
        print("1bhk")

class Father(GrandFather):
    Diamond = "22 Karet"
    def bhk2(self):
        print("2bhk")

class Son(Father):
    btc = "1BTC"
    def bhk3(self):
        print("3BHK")

s = Son()
f = Father()
gf = GrandFather()