'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line'''
for x in range(2000,3200):
    y=float(x % 7)
    z=float(x % 5)
    if (y==0.0) and (z<>0.0):
        print(x)
