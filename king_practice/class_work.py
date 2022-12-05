word = "Hello boss baby"
to_be_found = "b"
for i in range(len(word)):
    if word[i] == to_be_found:
        print(f"{to_be_found} was found in index {i}")
        print()
    # print(word[i], " --> ", i)
for i in range(len(word)):
     if word[i] != to_be_found:
        print(f"{word[i]} was found in index {i}")

print(word.replace('b', ''))
print(word.split('b'))

word = "Hello boss man"
for i, v in enumerate(word):
    if v == 'b':
        print()
        print(v, ':', i)

