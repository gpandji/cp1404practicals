# 1. Write code that asks the user for their name,
# then opens a file called name.txt and writes that name to it. Use open and close for this question.
name = input("Enter your name: ")

name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# 2. write code that opens "name.txt" and reads the name (as above) then prints (note the exact output)
name_file = open("name.txt", "r")
name = name_file.read().strip()
name_file.close()
print("Your name is", name)

# 3. Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers 17 42 400 on separate lines in the file and save it
with open("numbers.txt", "w") as numbers_file:
    numbers_file.write("17\n42\n400\n")

# Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59.
# Use with instead of open and close for this question
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    result = first_number + second_number
print(result)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers.
# Use with instead of open and close for this question.
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())
print(total)
