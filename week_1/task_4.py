# Create and write to a file
file = open("myfile.txt", "w")
file.write("Hello, I am learning Python.\n")
file.write("This is my file handling exercise.")
file.close()

# Reading the file
file = open("myfile.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()

# Addind new text to the file
file = open("myfile.txt", "a")
file.write("\nLearning file handling.")
file.close()

# Reading the updated file
file = open("myfile.txt", "r")
print("\nUpdated content:")
print(file.read())
file.close()