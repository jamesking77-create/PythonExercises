def convert_binary():
    user_input = int(input("convert any number to binary..."))
    binary = []
    mods = user_input % 2
    div = user_input // 2

    mod = div % 2
    binary.append(mods)
    binary.append(mod)
    while div > 1:
        div = div // 2
        mod = div % 2
        binary.append(mod)
    for i in binary:
        print(i)


print(convert_binary())


def covert_binary_to_number():
    sums = 0
    user_input2 = (input("covert binary to number..."))
    count = len(user_input2)
    for i in range(0, len(user_input2)):
        count -= 1
        result = 2 ** i * int(user_input2.__getitem__(count))
        # print(result)
        sums = sums + result
    print(sums)


print(covert_binary_to_number())
