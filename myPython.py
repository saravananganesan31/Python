# -----------------------------------------
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
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every # number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

text ="1,2,3,4,5"
l=text.split(",")
t=tuple(l)
print l
print t

output:
['1', '2', '3', '4', '5']
('1', '2', '3', '4', '5')
----------------------------------------- 
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

#!/bin/python3
n = int(input().strip())
a=n%2.0
if (a>=1):
    print("Weird")
elif (a==0) and n>=2 and n<=5:
    print("Not Weird")
elif (a==0) and n>=6 and n<=20:
    print("Weird")
elif n>20:
    print("Not Weird")
----------------------------------------- 
# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=int(input().strip())
b=int(input().strip())
c=a+b
d=a-b
e=a*b
print(c)
print(d)
print(e)
----------------------------------------- 
# Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .
# You don't need to perform any rounding or formatting operations.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, .

a=int(input().strip())
b=int(input().strip())
c=int(a/b)
d=float(a/b)
print(c)
print(d)

----------------------------------------- 
# Read an integer . For all non-negative integers , print . See the sample for details.

a=int(input().strip())
for i in range(0,a):
    b=i*i
    print(b)
----------------------------------------- 
# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

def is_leap(year):
    if ((year%4==0) and ((year%100) != 0) and (year%400==0)):
        leap = True
    else: leap=False
    return leap
year = int(input())
print(is_leap(year))
----------------------------------------- 
# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))
