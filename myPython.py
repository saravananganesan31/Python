-----------------------------------------
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line

for x in range(2000,3200):
    y=float(x % 7)
    z=float(x % 5)
    if (y==0.0) and (z!=0.0):
        print(str(x)+","),
-----------------------------------------        
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
x=int(input("enter no"))
y=factorial(x)
print(y),     
----------------------------------------- 

