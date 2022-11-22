# open('data.txt', 'w')
# Part 1
out_file = open('name.txt', 'w')

name = input("Please enter your name: ")
print(name, file=out_file)

out_file.close()

# Part 2
in_file = open('name.txt', 'r')

print(in_file.readline())

in_file.close()

# Part 3
in_file = open('numbers.txt', 'r')

first_number = in_file.readline()
second_number = in_file.readline(3)
total = int(first_number) + int(second_number)
print(total)
in_file.close()

# Part 4
in_file = open('numbers.txt', 'r')

first_number = in_file.readline()
second_number = in_file.readline(3)
third_number = in_file.readline(4)
total = int(first_number) + int(second_number) + int(third_number)
print(total)
in_file.close()
