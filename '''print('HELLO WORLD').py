print('HELLO WORLD')

A =float(input("Enter a no. :"))
S= float(input("Enter a no. :"))
C = float(input("Enter a no. :"))

print(A+S)
print(A-S)
print(A*S)
print(A/S)
print(A//S)
print(A%S)

if A>S and A>C:
    print(A)

elif S>C and S>A:
    print(S)
    
else:
    print(C)