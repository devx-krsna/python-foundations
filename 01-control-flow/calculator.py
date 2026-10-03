# Computational Thinking with Python - 26 Aug 2026
# picks the operation using if / elif / else

print("Calculator Program")

a= int(input("Enter the value 1: "))
b = int(input("Enter the value 2: "))

op = str(input("Enter the operation you want to do\n +,-,*,%,/\n"))

if op=='+':
    print(a+b)

elif op=='-':
    print(a-b)

elif op=='*':
    print(a*b)

elif op=='%':
    print(a%b)

elif op=='/':
    print(a/b)


