from math import factorial


n=int(input("size"))

for i in range(n):
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")

    print()
