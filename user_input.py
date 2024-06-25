# # a = int(input("""Enter your name : """))
# #
# # a=str(a)
# #
# # print("a :", a)
# # print("a data type :", type(a))
#
#
# # typecasting:
# # string to int - works only that string contains only numbers - for float also
# # int to string we can do
# # float to string
# # string to float - only float values
#
# # FIRST_CLASS = 70
# # SECOND_CLASS = 60
# # PASS = 35
# #
# # a = int(input("Enter your marks : "))
# #
# # if (a >= FIRST_CLASS):
# #     print("First class")
# # elif (a >= SECOND_CLASS):
# #     print("Second class")
# # elif (a >= PASS):
# #     print("pass")
# # else:
# #     print("Fail")
#
#
# # OPerator precedence
#
# # 1. ()
# # 2. **
# # 3. * / % //
# # 4. + -
# # 5. =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
#
# a = 78
# b = 56
# c = 34
# d = 12
# e = 34
#
# # print(a ** b + c * d % e)
# print(a  + a * 2+ b)
#
#
# # 78+56+156 = 290


# slicing

a = "hello world to the python family, welcome, to"
# print(h)
# print(h.count("or8"))
# r = h.replace("world","Python Family")
# print(r)
# f=a.split(",")
# for i in f:
#     print(i)

# f = ["hi", "welcome", "to", "hyderabad"]
# print(f)
# j = " -  & ".join(f)
# print(j)


# a = input("Please enter your name :")
a = "ramu is a a gooD boy"

print("Normal output : ",a)
print("lower output : ",a.lower())
print("upper output : ",a.upper())

print("capitalize output : ",a.capitalize())
print("title output : ",a.title())
print("swapcase output : ",a.swapcase())


if a == "ramu":
    print("ramu")
else:
    print("not ramu")
