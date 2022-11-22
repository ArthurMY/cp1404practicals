# part a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# part b
for n in range(20, 0, -1):
    print(n, end=' ')
print()

# part c
number = int(input("Number of stars: "))
print(f"{number * '*'}")

# part d
starnumber = int(input("Number of stars: "))
for line in range(1, starnumber+1):
    print(line * '*')
