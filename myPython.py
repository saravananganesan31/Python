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
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

x=int(input("enter no : "))
print(x)
d=dict()
for i in range(1,x+1):
            d[i]=i*i
print(d)

enter no : 10
10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
----------------------------------------- 




