# Computational Thinking with Python - CA1, 9 Sep 2026

#Program 1 Finding Grades via Marks

marks = int(input("Enter your marks: "))

if marks>=90:
    print("You have got Grade A")

elif marks>=80:
    print("You have got Grade B")

elif marks>=70:
    print("You have got Grade C")

elif marks>=60:
    print("You have got Grade D")

else:
    print("You have got Grade F")


#Program 2 Finding Area of the Rectangle

print("\n")

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

area = length * breadth

print("Area of the Rectangle is: ", area)
