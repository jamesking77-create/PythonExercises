import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range(60_000):
    random_rolls = random.randint(1, 6)
    if random_rolls == 1:
        frequency1 += 1
    elif random_rolls == 2:
        frequency2 += 1
    elif random_rolls == 3:
        frequency3 += 1
    elif random_rolls == 4:
        frequency4 += 1
    elif random_rolls == 5:
        frequency5 += 1
    elif random_rolls == 6:
        frequency6 += 1
print(f"{'faces':<10}{'frequency':>15}")
print(f"1{frequency1:>20}\n2{frequency2:>20}\n3{frequency3:>20}\n4"
      f"{frequency4:>20}\n5{frequency5:>20}\n6{frequency6:>20}")

#     print()
