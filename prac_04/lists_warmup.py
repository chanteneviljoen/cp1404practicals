numbers = [3, 1, 4, 1, 5, 9, 2]
# 3
print(numbers[0])

# 2
print(numbers[-1])

# 1
print(numbers[3])

# [3, 1, 4, 1, 5, 9]
print(numbers[:-1])

# [1]
print(numbers[3:4])

# true
print(5 in numbers)

# false
print(7 in numbers)

# false
print("3" in numbers)

# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers + [6, 5, 3])

"""Write Python expressions (in the same Python file) to achieve the following:"""

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Get all the elements from numbers except the first two (slice)
print(numbers[2:])
# Check if 9 is an element of numbers
print(9 in numbers)
