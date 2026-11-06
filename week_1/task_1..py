
# To Print a message
print("Hello, Python!")

# To Store a name and display it
name = "Sugam"
print("My name is", name)

# To Add two numbers
first_number = 12
second_number = 8
print("Sum:", first_number + second_number)

# To Check whether a number is positive, negative or zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("The number is zero")

# To Check whether a number is even or odd
number = int(input("Enter another number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# To Print numbers from 1 to 10
for number in range(1, 11):
    print(number)

# To Print a multiplication table
number = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# To Find the sum of numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print("Total from 1 to 100:", total)
