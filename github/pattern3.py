l=6
k=65
for i in range(7):
    for space in range(l):
        print("",end=" ")

    for alpha in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    for space in range(l):
        print("",end=" ")

    print()
    l=l-1
