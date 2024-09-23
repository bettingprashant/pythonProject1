#1

# def func(i,j):
#     print(i,j)
#
# # func(10,20)
# func(j=20,i=10)

#2

# def func(i,j =10):
#     print(i,j)
# func(100,200)
# func(100)

#3

# def greetings(name,greetmsg):
#     print(greetmsg+"  "+name)
# greetings(name='Prashant',greetmsg='Hello')
# greetings(greetmsg='Hello',name='Prashant')

#4

# def my_func(a,b,c):
#     print(a,b,c)
# my_func(10,20,30)
# my_func(a=10,b=20,c=30)
# my_func(b=20,a=10,c=30)
# my_func(b=20,a=10,c=30)
# my_func(10,20,c=30)

#5

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

# print (largest(100,200))
# print(largest(20,20))

res=largest(20,10)
print(res)
print(type(res))