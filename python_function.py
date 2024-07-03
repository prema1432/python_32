# functins
# 1. reusability
# 2. Modurality
# 3.Abstarction
# Mainability
# scalability
# collabaritions
# clarity


# print(" Hai welcome to python , Mr Rakesh")
# print(" Hai welcome to python , Mr mahesh")
# print(" Hai welcome to python , Mr Suresh")
# print(" Hai welcome to python , Mr Priya")
# print(" Hai welcome to python , Mr Yamuna")
# print(" Hai welcome to python , Mr Mohan")
# print(" Hai welcome to python , Mr Alluarjun")
# print(" Hai welcome to python , Mr Vikas")
# print(" Hai welcome to python , Mr Anajani")

# def greetings(name):
#     print(f" Hai welcome to python , Mr {name}")
#
#
# greetings("Rakesh")
# greetings("mahesh")
# greetings("Suresh")

# python - 2 types of functions

# 1.Built in functions
# id()
#
# print()
# type()
# input()
# eval()
# ....


# 2.User Defined Functions

# def functyion_name():
#     # print("Hai h")
#     return True
#
#
# functyion_name()

# Parameters

# def sample_fun(age):
#     print(f"Yourrr age is {age*5} Multiplyed by 5")
#
# sample_fun(45)

# Types of arguments
# 1. Positional
# 2. Keyword
# 3. Default
# 4. Variable length


# 1. Positional Arguments:
# def jio(a,b,c,d,e,f):
#     print(a,b,c,d,e,f)
#

# jio(1,2,3,4,5,6)


# def subs(a, b):
#     print(a - b)
#
#
# subs(5)

# 2.keyword arguments

# def sub(a, b):
#     print(a - b)
#
#
# sub(b=5, a=18)


# .default arguments

# def hello(a="SSample Name"):
#     print(f"Hai {a}")
#
#
# hello("raviteja")

# variable length arguments
# def hello(*a,b):
#     print(sum(a)*b)
#
#
# #
# hello(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,b=10)


# keyword arguments multiple
# def display(**kwargs):
#     # print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
#
#
#
# display(name="mahesh", age=23, place="chennai")


# h = 10
# print(h)
# # 2 typess of variables
# # 1. Global
# # 2. Local
#
# a = 10
#
#
# def samp():
#     print(a)
#
#
# def rammm():
#     a = 77
#     print(a)
#
#
# samp()
# rammm()
#
#
# def jii():
#     b = 35
#     print(b)
#
#
# def shayma():
#     b=36
#     print(b)
#
#
# jii()
# shayma()
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# # print(factorial(5)) = 5*factorial(4)
# # = 5*4*factorial(3)
# # =5*$=4*3*factorial(2)
# # =5*4*3*2*factorial(1)
# # =5*4*3*2*1
#
#
# print(factorial(5))


# lambda
# lambda n:n*n
# dd = lambda n: n * n
# print(dd(5))
#
# ssss = lambda a, b: a + b
# print(ssss(5, 6))
