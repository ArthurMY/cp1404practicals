number = int(input("Number of items: "))
total = 0
while number <= 0:
    print("Invalid number")
    number = int(input("Number of items: "))

for n in range(number):
    price = float(input("Price of item: "))
    total += price


if total > 100:
    total *= 0.9

print(f"Total price for {number} items is ${total:.2f}")
