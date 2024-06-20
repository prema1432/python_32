# # today we are disccuing the DATA TYPES in Python.
#
# # Data types
# # 1. int - whole number 0 - 999999999999 , Ex: 9999999999999
#
#
# # 2. float - deciamls formats, Ex: 999999999.333333
#
# # 3. complex - scientific notation applications and elecertical engineering
#
# # a+bj
#
# # a = Real part
#
# # bj = Imaginary part
#
# # 3+5j
#
#
# # 4. bool  == True or False
#
# # if,while,True,False,None
#
# # a=0
# # print(type(a))
# # print(a)
# # print(bool(a))
#
#
# # 5. str
# # a=("hai "
# #    "welcome"
# #    "to"
# #    "python")
# # print(a)
# # print(type(a))
# # b = 'prema  '
# # print(type(b))
# # print(b)
# # c = """prema"""
# # d = '''Hai Welcome
# # to
# # python
# # '''
# # print(type(d))
# # print(d)
#
# # Hai Welcome
# # to
# # python
#
#
# a = "Welcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to python"
#
# # print(a)
# # print(type(a))
# # []
#
# a = "welcome"
# # left to right -> +ve ---0 t0 to
# # right to left -> -ve
# # print(a[-3:])  ---1
# # 6. list
# # a = ["welcome", "to", "python", 1, 2, 3, True,
# #      False]  # group of values,insertion order required,duplicate allowed, ordered
# #
# # print(a)
# # # for i in a:
# # #     print(f"{i} Hey Hai ")
# #
# # print(a[0:2])
# #
# # a.append("Mahesh")
# # print(a)
# #
# # a.remove("welcome")
# # print(a)
# # b=a*2
# # print(b)
#
#
#
#
#
# # 7. tuple
# # ()
# a=("naveen","kumar")
# print(a)
# print(type(a))
#
# # a.append("mahesh")
# # print(a)
#
# # 8. dict
# # key  value pairs
# # a={"name":"mohan","age":23,"male": True,"name":"ramu","place":"ramu"}
# # print(a)
# # print(type(a))
# # a["locaiton"]="chennai"
# #
# # print(a)
# # a["age"]=88
# # print(a)
# # 9. set
# # p={1,2,3,4,5,6,7,8,9,1,1,2,2,4,99,88,1,1,1,1,1,1,1}
# # print(p)
# # print(type(p))
# # p.add(123)
# # print(p)
# # p.remove(2)
# # print(p)
#
#
# # checklist = [1,2,3,4,5,6,7,8,9,1,1,2,2,4,99,88,1,1,1,1,1,1,1]
# #
# # expected_output= [1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 88, 123]
#
# # 10. frozenset
# # s={10,20,30,40}
# # print(s)
# # print(type(s))
# # h=frozenset(s)
# # print(h)
# # print(type(h))
#
# # h.add(67)
# # print(h)
#
#
#
#
# # 11. bytes
# x=[10,30,80]
#
# y=bytes(x)
# print(y)
# print(type(y))
#
# # 12. bytearray
#
#
# x=[10,30,80]
#
# y=bytearray(x)
# print(y)
# print(type(y))
#
# # 13. NoneType
#
#
# a = None
# print(a)
# print(type(a))
#
#
# # a = 100.50
# # print("my name is " + a)
# # print(type(a)) # data tyep - which data type
# # a = 3
# # print(a)
# # print(id(a)) # id of the object variable
# # b = 44
# # print(b)
# # print(id(b))
# #
# # A = 77
# # print(A)
# # print(id(A))


# Escape Character
s = "Wellcome to \bpython"
print(s)

# \n = new line
# \t = tab
# \b = backspace
# \r = carriage return
# \f = form feed
# \a = alert
# \v = vertical tab
# \' = single quote
# \" = double quote
# \? = question mark

# jkk = "Welcome to \bpython"
# print(jkk)
#
# MAX_PRICE =200
#
# a=67
# if a == MAX_PRICE:
#     print("Hey U enter 78")
# elif a <= MAX_PRICE:
#     print("Hey u below 23")
# else:
#     print("Hey Finally I am here")


# Airthmatic Operator
# +, -, *, /, //, %, **
a = 13
b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# Relational Operator
# <, >, <=, >=, ==, !=
# a = 13
# b = 5
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)
# print(a != b)

# =
# Equality Operator
# is, is not, in, not in
# a = 13
# b = 56
# print(a is b)
# print(a is not b)
# f = [1, 2, 35, 56, 7676, 10, 13]
# print(a in f)
# print(b not in f)

# Logical Operator
# and, or, not
a = 13
b = 56
# print(a > 10 and b < 10)
# print(a > 10 or b > 10)
# print(not a > 10)
c = 4
# print(a < 10 and b < 10 or c > 10)
# False and False or False
# Falkse or False

# d="welcome" and "python  " and  "world"
# print(d)

# Assignment Operator
# =, +=, -=, *=, /=, //=, %=, **=
# a = 13
# a += 10
# print(a)
# a -= 10
# print(a)
# a *= 10
# print(a)
# a /= 10
# print(a)
# a //= 10
# print(a)
# a %= 10
# print(a)
# a **= 10
# print(a)

a = 10
b = a + 10
# print(b)
#
#
# a=10
# a+=10
# # a=a+10
# print(a)


# Ternary Operator
a = 10
b = 20
# print(a if a > b else b)
# if a>b:
#     print(a)
# else:
#     print(b)