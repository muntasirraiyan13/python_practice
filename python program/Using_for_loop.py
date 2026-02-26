x = int(input("Enter a number: "))
tup = (1, 2, 3, 4, 56, 7)

for value in tup:
    if (value == x):
        print("The number is found")
        break
else:
    print("Sorry!the number is not found")
