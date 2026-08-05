
num = 1
while (num <= 4):
    print("*" * num)
    num+= 1

num = 1
for num in range(1, 11):
    print(num)

num1 = 1
for num1 in range(1, 10, 2):
    print(num1)

num2 = 2
for num2 in range(2, 11, 2):
    print(num2)

name =  "Jhone Doe"
for char in name:
    print(char)

num = 4
while (num >= 1):
    print("*" * num)
    num= num - 1

rows = 4
for n in range (1, rows + 1):
    spaces = rows - n
    stars = 2 * n - 1
    print(" " * spaces + "*" * stars) 

