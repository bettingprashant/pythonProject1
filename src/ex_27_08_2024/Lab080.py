def my_decorator(func):

    def wrapper():
        print("something is happening before the function is called.")
        print("Add Helmet, Dashcash,gloves,Knee guards")
        func()
        print("Something is happening after the function is called")
        print("secure Driving")
    return wrapper()

@my_decorator
def drive_bike():
    print("I am driving")

# drive_bike()