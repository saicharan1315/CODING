def circle(n):
    row = n
    col = n
    for i in range(row):
        for j in range(col):
            if i==j or (i+j) == n-1:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
circle(4)