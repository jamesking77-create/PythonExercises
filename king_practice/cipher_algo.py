import string

# print(string.ascii_lowercase)
user_input = input("Enter a word to decode: ")
key = int(input("What key do want us to use >>> "))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
decode_lower = lower_case[key:] + lower_case[:key]
decode_upper = upper_case[key:] + upper_case[:key]
letters = lower_case + upper_case + string.whitespace
decode_letters = decode_lower + decode_upper + string.whitespace
encode = user_input.translate(str.maketrans(letters, decode_letters))
decode = encode.translate(str.maketrans(decode_letters, letters))
print(encode)
print(decode)

