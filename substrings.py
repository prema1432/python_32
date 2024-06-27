# a = " "
#
# print(a)
# # print(a.startswith("prerma"))
# # print(a.endswith("welcome"))
# #
# # # check if a string is present in another string
# # print(type(a))
# # if type(a) == "string":
# #     print("true")
# # else:
# #     print("false")
#
# # isalnum == (a to z, A to Z, 0 to 9)
# # isalpha == (a to z, A to Z)
# # isdigit == (0 to 9)
# # isspace == (white space)
# # islower == (a to z)
# # isupper == (A to Z)
# # istitle == (First letter is capital)
#
# # print("is alnum", a.isalnum())  # false
# # print("is alpha", a.isalpha())  # false
# # print("is digit", a.isdigit())  # false
# # print("is space", a.isspace())  # false
# # print("is lower", a.islower())  # true
# # print("is upper", a.isupper())  # false
# # print("is title", a.istitle())  # false
#
#
# # Output Formatorts
#
# # s = "Priya"
# # a = "Naveen"
# # z = 500
#
# # print("{0} and  {1} both are friends. they have {2} amount.".format(s, a, z))
#
# # print(f"{s} and  {a} both are friends. they have {z}% amount.")
#
# # print(s + " and " + a + " both are friends. they have " + str(z) + " amount.")
#
# # print("%s and %s both are friends. they have %s amount." % (s, a, z)) -- logger
#
#
# apple = "apples are good for health and it is very healthy"
# print(apple.count("a"))
#
# print(apple[::-1])
#
# print("".join(reversed(apple)))
# # print(reversed(apple))
#
# apple_length = len(apple) - 1
# output = ""
#
# while apple_length >= 0:
#     output += apple[apple_length]
#     apple_length -= 1
# print(output)

# g=[10,20,25,30,45,832,23432,4324,23,423,4]
# g.reverse()
# # g.sort(reverse=True)
# print(g)
#
# jjj=["zillan","madfhavan","ameer","Aarthi","aarthi2","999"]
# print(jjj)
# jjj.sort()
# print(jjj)


r = [10, 20, 30, 11]
s = [10, 20, 30, 11]
# s=[40,50,60,11]
print(r + s)

print(r * 3)

if r == s:
    print("same")
else:
    print("not same")

print(300 in r)

hh = [10, 20, 30, [45, 50, [76767]]]
print(hh)
print(hh[3])
print(hh[3][2])

# list of compression

d = [x for x in range(1, 100) if x % 2 == 0]
print(d)

# for a in range(10):
#     if a%2==0:
#
