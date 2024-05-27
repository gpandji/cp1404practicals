name = (input("password: "))
while len(name) < 3:
    name = (input("please re-enter password: "))
password = '*' * len(name)
print(f"password: {password}")