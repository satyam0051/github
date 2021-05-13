for i in range(1,6):
    for j in range(1,6):
        if ((i+j==4 and i<=3) or ((i-j==2) and i>3) or ((j-i==2) and j>3) or (i==4 and j==4)):
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
