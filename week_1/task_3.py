# Day 3 : functions

# Function to add two numbers
def add_numbers(a, b):
    return a + b

print("Addition:", add_numbers(10, 5))


#  Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

test_number = int(input("Enter a number to check if it is prime: "))
if is_prime(test_number):
    print("Prime number")
else:
    print("Not a prime number")


#  Function to calculate the average of a list
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

marks = [75, 80, 68, 90, 85]
print("Average marks:", calculate_average(marks))
