# task_2 : Lists and dictionaries

# To Create a list and print each item
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(fruit)

# To Find the largest number in a list
numbers = [12, 45, 7, 89, 23]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest number:", largest)

# To Find the smallest number in a list
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest number:", smallest)

# To Count how many even numbers are in a list
values = [2, 5, 8, 11, 14, 17, 20]
even_count = 0
for value in values:
    if value % 2 == 0:
        even_count += 1
print("Even numbers:", even_count)

# To Remove duplicate values from a list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print("Without duplicates:", unique_items)

# To Create a dictionary for a student
student = {
    "name": "Ram",
    "age": 22,
    "course": "Computer Engineering"
}
print("Student name:", student["name"])

# To Loop through dictionary keys and values
for key, value in student.items():
    print(key, ":", value)

# To Count how many times each word appears
sentence = "Machine Learning is the branch of AI. We are learning machine learning basics."
word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word count:", word_count)
