m=6
k=65
n=0
l=5
for i in range(11):
    if i<5:
        for space in range(l):
            print("",end=" ")
        for alpha in range(65,66+i):
            print(chr(alpha),end=" ")
    
        for space in range(l):
            print("",end=" ")
        l=l-1
    else:
        for space in range(n):
            print("",end=" ")
        for alpha in range(m):
            print(chr(k),end=" ")
            k=k+1
        for space in range(n):
            print("",end=" ")
        n=n+1
        m=m-1
    print()
