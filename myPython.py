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
----------------------------------------- 
# Read an integer .
# Without using any string methods, try to print the following:
# Note that "" represents the values in between.

a=int(input())
for i in range(a):
    print(i+1,end='')
   
----------------------------------------- 
# zeros
# The zeros tool returns a new array with a given shape and type filled with 's.
# import numpy
# print numpy.zeros((1,2))                    #Default type is float
# Output : [[ 0.  0.]] 
# print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
# Output : [[0 0]]
# ones
# The ones tool returns a new array with a given shape and type filled with 's.
# print numpy.ones((1,2))                    #Default type is float
# Output : [[ 1.  1.]] 
# print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
# Output : [[1 1]]   
# Task - You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

import numpy
N = tuple(map(int,input().strip().split()))
z = numpy.zeros(N, dtype=numpy.int)
o = numpy.ones(N, dtype=numpy.int)
print (z)
print (o)
----------------------------------------- 
# The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.
# import numpy
# print numpy.identity(3) #3 is for  dimension 3 X 3
# Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
# [ 0.  0.  1.]]
# eye
# The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
# import numpy
# print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.
# Output
# [[ 0.  1.  0.  0.  0.  0.  0.]
#  [ 0.  0.  1.  0.  0.  0.  0.]
#  [ 0.  0.  0.  1.  0.  0.  0.]
#  [ 0.  0.  0.  0.  1.  0.  0.]
#  [ 0.  0.  0.  0.  0.  1.  0.]
#  [ 0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.  0.]]
# # print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
# Task
# Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

----------------------------------------- 


print("hello world")
#print ("how are you doing")
count=100
miles=1200.342
name="Saravanan"
var=124242
var1=4242.4248204820
print(var+float(var1))
a=42
b=4242
c="424"
d=int(c)
e=float(c)
f=str(a)
print(d)
print(name)
print(f)
v="Saravanan Ganesan"
print(v[0:10])
a="Saravanan"
b="Ganesan"
print(a+"***"+b)

print((a+b)*3)
print("A" in "Saravanan")


lister=[1,2,3,4,5,6,7,8,1,"Saravanan","Saravanan", "Santanu", "Kanishka",1,111]
lister.append("Pappathi")
print(lister.count(1))
print(lister)
dictionary={}
tel={"Saravanan":4256558840,"Pappathi":8754417708,"Gopal":9894050719,"Kanishka": 7338825997}
print(tel)
tel['Gopal']

tup1=("saravanan","Ganesan","Kanishka",1,3,4,5,653,"Durairaj")
print(tup1[5:8])

tuper=(1,2,3,4,5,6,7,8,9,10)
for x in tuper:
    print(x)

tuper101=("Saravanan",7338825997)
x,y=tuper101
print(x)
print(y)
temp=x
x=y
y=temp
print(x)
print(y)
x,y=y,x
print(x)
print(y)

friends=["x","Kanishka","Santanu","Kanishka","Selvaraj", "Maniraj"]
people ={"x":733,"Kanishka":996,"Santanu":989}
print(people[friends[2]])

var=1245
if (var == 1242424):
    print("True")
else:
    print("False")

mystring="SaravananGanesanSatanuKanishka"
if "*" in mystring:
    print("G char available in ",mystring)
elif "7" in mystring:
    print("S char available in ", mystring)
elif "0" in mystring:
    print ("K char available in ", mystring)
else:
    print("not fall under any of above condition")

for x in range(1,12):
   for y in range(1,11):
    print(x,y,x*y)

p = 10
q = 10
while (p >= 0 ):
    while (q >= 0):
        print(p,q,p*q)
        p -=1
        q -=1
print("while loop exit")

v=5
while True:
    v -=1
    if (v==3):
        continue
    print(v)
    if (v==0):
        break

k= int(input("Enter your age"))
s=str(input("Enter your name"))
print(k)
print(string)



class Student:
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
class Marks:
    def __init__(self,rollno, tamil, english, maths, science, social_science):
        self.rollno=rollno
        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.social_science=social_science
        self.total=self.tamil+self.english+self.maths+self.science+self.science+self.social_science

obj1=Student("saravanan",101,1)
print obj1.name,obj1.rollno,obj1.dept

obj2=Marks(101,60,80,90,75,85)
obj2=Marks(102,70,65,95,78,77)

print obj2.rollno,obj2.total

-------------------------------------------------------------------------------


print("hello world")
#print ("how are you doing")
count=100
miles=1200.342
name="Saravanan"
var=124242
var1=4242.4248204820
print(var+float(var1))
a=42
b=4242
c="424"
d=int(c)
e=float(c)
f=str(a)
print(d)
print(name)
print(f)
v="Saravanan Ganesan"
print(v[0:10])
a="Saravanan"
b="Ganesan"
print(a+"***"+b)

print((a+b)*3)
print("A" in "Saravanan")


lister=[1,2,3,4,5,6,7,8,1,"Saravanan","Saravanan", "Santanu", "Kanishka",1,111]
lister.append("Pappathi")
print(lister.count(1))
print(lister)
dictionary={}
tel={"Saravanan":4256558840,"Pappathi":8754417708,"Gopal":9894050719,"Kanishka": 7338825997}
print(tel)
tel['Gopal']

tup1=("saravanan","Ganesan","Kanishka",1,3,4,5,653,"Durairaj")
print(tup1[5:8])

tuper=(1,2,3,4,5,6,7,8,9,10)
for x in tuper:
    print(x)

tuper101=("Saravanan",7338825997)
x,y=tuper101
print(x)
print(y)
temp=x
x=y
y=temp
print(x)
print(y)
x,y=y,x
print(x)
print(y)

friends=["x","Kanishka","Santanu","Kanishka","Selvaraj", "Maniraj"]
people ={"x":733,"Kanishka":996,"Santanu":989}
print(people[friends[2]])

var=1245
if (var == 1242424):
    print("True")
else:
    print("False")

mystring="SaravananGanesanSatanuKanishka"
if "*" in mystring:
    print("G char available in ",mystring)
elif "7" in mystring:
    print("S char available in ", mystring)
elif "0" in mystring:
    print ("K char available in ", mystring)
else:
    print("not fall under any of above condition")

for x in range(1,12):
   for y in range(1,11):
    print(x,y,x*y)

p = 10
q = 10
while (p >= 0 ):
    while (q >= 0):
        print(p,q,p*q)
        p -=1
        q -=1
print("while loop exit")

v=5
while True:
    v -=1
    if (v==3):
        continue
    print(v)
    if (v==0):
        break

k= int(input("Enter your age"))
s=str(input("Enter your name"))
print(k)
print(string)



class Student:
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
class Marks:
    def __init__(self,rollno, tamil, english, maths, science, social_science):
        self.rollno=rollno
        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.social_science=social_science
        self.total=self.tamil+self.english+self.maths+self.science+self.science+self.social_science

obj1=Student("saravanan",101,1)
print obj1.name,obj1.rollno,obj1.dept

obj2=Marks(101,60,80,90,75,85)
obj2=Marks(102,70,65,95,78,77)

print obj2.rollno,obj2.total

-------------------------------------------------------------------
