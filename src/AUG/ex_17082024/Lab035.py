import math

radius = float(input("Enter the radius of the circle\n"))
print(radius)
area = math.pi*math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle is  ->", area)
print("Area of the circle is  ->", area2)
print(f"Area of the circle is  -> {area:.2f}")


print(3.141592653589793*(float(input("Enter the radius\n"))**2))