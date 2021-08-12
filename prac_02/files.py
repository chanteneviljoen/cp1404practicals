# 1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# 3
in_file = open("numbers.txt", "r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
print(number_one + number_two)

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print("Total: ", total)
