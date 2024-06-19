# today we are disccuing the DATA TYPES in Python.

# Data types
# 1. int - whole number 0 - 999999999999 , Ex: 9999999999999


# 2. float - deciamls formats, Ex: 999999999.333333

# 3. complex - scientific notation applications and elecertical engineering

# a+bj

# a = Real part

# bj = Imaginary part

# 3+5j


# 4. bool  == True or False

# if,while,True,False,None

# a=0
# print(type(a))
# print(a)
# print(bool(a))


# 5. str
# a=("hai "
#    "welcome"
#    "to"
#    "python")
# print(a)
# print(type(a))
# b = 'prema  '
# print(type(b))
# print(b)
# c = """prema"""
# d = '''Hai Welcome
# to
# python
# '''
# print(type(d))
# print(d)

# Hai Welcome
# to
# python


a = "Welcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to pythonWelcome to python"

# print(a)
# print(type(a))
# []

a = "welcome"
# left to right -> +ve ---0 t0 to
# right to left -> -ve
# print(a[-3:])  ---1
# 6. list
# a = ["welcome", "to", "python", 1, 2, 3, True,
#      False]  # group of values,insertion order required,duplicate allowed, ordered
#
# print(a)
# # for i in a:
# #     print(f"{i} Hey Hai ")
#
# print(a[0:2])
#
# a.append("Mahesh")
# print(a)
#
# a.remove("welcome")
# print(a)
# b=a*2
# print(b)





# 7. tuple
# ()
a=("naveen","kumar")
print(a)
print(type(a))

# a.append("mahesh")
# print(a)

# 8. dict
# key  value pairs
# a={"name":"mohan","age":23,"male": True,"name":"ramu","place":"ramu"}
# print(a)
# print(type(a))
# a["locaiton"]="chennai"
#
# print(a)
# a["age"]=88
# print(a)
# 9. set
p={1,2,3,4,5,6,7,8,9,1,1,2,2,4,99,88,1,1,1,1,1,1,1}
print(p)
print(type(p))
p.add(123)
print(p)
p.remove(2)
print(p)


checklist = [1,2,3,4,5,6,7,8,9,1,1,2,2,4,99,88,1,1,1,1,1,1,1]

expected_output= [1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 88, 123]

# 10. frozenset
# 11. bytes
# 12. bytearray
# 13. NoneType

# a = 100.50
# print("my name is " + a)
# print(type(a)) # data tyep - which data type
# a = 3
# print(a)
# print(id(a)) # id of the object variable
# b = 44
# print(b)
# print(id(b))
#
# A = 77
# print(A)
# print(id(A))
