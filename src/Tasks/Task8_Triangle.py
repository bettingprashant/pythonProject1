#Triangle classifier

a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))

if a == b == c:
    print("Equlateral")
elif a ==b or b ==c or a ==c:
    print("isosceles")
else:
    print("Scalene")
