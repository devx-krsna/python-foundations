# Computational Thinking with Python - 16 Sep 2026

num = int(input("Enter a number of which you want factorial: "))

# fact holds the product so far
fact = 1

for i in range(1,num+1):
    fact = fact * i
    
    
    print(fact)
