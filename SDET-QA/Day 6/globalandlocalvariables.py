#1
global_var=20

# def func():
#     local_var=10
#     print(local_var)
#     print(global_var)
#
# func()
#
# print(global_var)

#2

# xy=100
#
# def cool():
#     global xy
#     xy=200
#     print(xy)
# cool()

#3
#
# xy=100
# def cool():
#     global xy
#     xy=200
#     print(xy)
# cool()
# print(xy)

#4

# x=100
# def cool():
#     global x
#     x = 500
#     print(x)
# # cool()
# print(x)

#5
def cool():
    global x
    x=100
    print(x)

cool()
print(x)