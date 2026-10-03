# Computational Thinking with Python - 2 Sep 2026
# end="" stops print() from adding a new line

n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
