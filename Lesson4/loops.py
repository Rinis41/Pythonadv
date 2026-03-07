names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print(name)

for number in range(1, 6):
    print(number)

numbers = [12, 45, 6, 72, 21, 8, 94, 57]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("This is maximum value in the list: ", maximum)

count = 1

while count <= 5:
    print("iteration", count)
    count += 1

numbers = [1, 2, 4, 5, 6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found!")
        break

scores = 68, 42, 57, 78, 35, 62, 50, 92]
total = 0
count = 0

for score in scores