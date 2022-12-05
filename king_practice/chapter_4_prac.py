# j = "james"
# to_be_found = "a"
# for i in range(len(j)):
#     if j[i] == to_be_found:
#         print(f"{to_be_found} was found in index {i}")
#     else:
#         print(f"sorry i could not find your '{to_be_found}'")

# j = "james"
# to_be_found = "m"
#
# for index, char in enumerate(j):
#     if char == to_be_found:
#         print(f"{char} found at index {index}")
#         break
#     else:
#         print(-1)


# STRING_METHODS

hello = "Hello there!!!"
print(hello.find("l"))
print(hello.index("o"))
print(hello.upper())

hello = "#####Hello Has world#####"
print(hello.rfind("o"))
print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.casefold())
print(hello.swapcase())
print(hello.capitalize())
print(hello.count("l"))
print(hello.lower().count("h"))
print(hello.center(30, "|"))
print(hello.ljust(30, "|"))
print(hello.rjust(30, "|"))
print(hello.endswith("H"))
print(hello.replace("l", "t", ))
print(hello.strip("#"))
print(hello.zfill(30))
print(hello.split('Has'))
print(hello.partition("lo"))
print(hello.removeprefix('#####Hello'))
print(hello.removesuffix('world#####'))
#
for i in range(1, 21, 2):
    asterisk = "*" * i
    print(asterisk.center(20))
merry = "merry christmas"
print(merry.upper().center(19, "*"))
for i in range(1, 3):
    asterisk = "***"
    print(asterisk.center(20))
#
# print("-".join(["a", "b", "c"]))
#
# bin_ = "100001010101010005667"
# print(bin_.replace("1", "x").replace("0", "1").replace("x", "0"))
# print(bin_.translate(str.maketrans("10", "01", "6")))
#
#

#
# c = float(input("enter the current temperature in celsius: "))
# def far_to_cel(c):
#     return c * 1.8 + 32.0
# print('your temperature in fahrenheit is: ' + str (far_to_cel(c)))


# def name(z):
#     return 'zainab is a beautiful lady'
# print(name(z=""))

#
# lst = (input("Enter three to five separate numbers: "))
#
#
# def is_unique():
#     for each in (lst[:3]):
#        return is_unique(  each % 2 == 0)
#     print(lst+"is an outlier")


# number = '100001101001001'
#
#
# def number_swap(number):
#     return number.replace("1", "x").replace("0", "1").replace("x", "0")
#
#
# print(number_swap(number))
#
# j = "james"
# for i in j:
#     print(j)
