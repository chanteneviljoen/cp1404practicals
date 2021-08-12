import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? 5
# What was the smallest number you could have seen, what was the largest? 5 - smallest, 19 - largest

# What did you see on line 2? 7
# What was the smallest number you could have seen, what was the largest? 3 -smallest, 9 - largest
# Could line 2 have produced a 4? no

# What did you see on line 3? 4.873392853252598
# What was the smallest number you could have seen, what was the largest? 2.5 - smallest, 5.5 - largest

print(random.randint(1, 100 + 1))
