# 1--->To find the largest of three numbers
'''
a= int (input())
b=int(input())
c=int (input())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
'''

#2---> To find the second largest number
""""
a= int (input())
b=int(input())
c=int (input())
if a>b and a>c:
    if b>c:
        print(b)
elif b>a and b>c:
    if a>c:
        print(a)
else:
    print(c)
"""

"""
# largest of two 
a= int (input())
b=int(input())
c=int (input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a > b and a > c:
        print(a)
elif b > c:
        print(b)
else:
        print(c)
"""

# 3---> To print hello world for 1000 times
'''
x= "hello world"
for i in range(1000):
   print(x)
'''


# 4---> To print the relation between two integers
'''
a,b = input().split()
if a>b:
    print("a > b")
elif b>a:
    print(" b > a")
elif a==b:
    print(" a == b")
'''


# 5---> To find if it is triangle
'''
a,b,c = input().split()
if (a+b>c):
    print("Yes")
elif (b+c>c):
    print("Yes")
elif (a+c>b):
    print("Yes")
else:
    print("No")
'''

# 6---> To find the remaining apples in the basket
"""
n= int(input())
k=int(input())
"""

# 7---> To find the reverse of a string
"""
n= int(input())
if n>0:
    res = 0
    while n > 0:
        r = n%10
        res = (res*10) + r
        n = n//10
    print(res)
elif n == 0:
    print(n)
else:
    res = 0
    n = n * -1
    while n > 0:
        r = n % 10
        res = (res * 10) + r
        n = n // 10
    print(res * -1)
"""

# 8---> watermelon into two even weights
'''
w = int(input())
if w > 2 and w% 2 == 0:
        print("Yes")
else:
        print("No")
'''

# 9---> Fever in F and no of test cases
# Approach-1
'''
T = int(input("Enter the number of test cases: "))
for i in range(T):
    temp = int(input("Enter the temerature"))
    if(temp > 98):
        print("yes")
    else:
        print("no")
'''
#Approach-2
'''
T = int(input("Enter the number of test cases: "))
while T> 0:
    temp = int(input("Enter the temerature"))
    if (temp > 98):
        print("yes")
    else:
        print("no")
'''

# 10 ---> By discount find the remaining price
# only if sp is below 100
'''
t= int(input())
for i in range(t):
    d= int(input())
    print(100-d)
'''

# 11 ---> TV discount given 2 sp and their discounts
"""
t=int(input("enter the number of test cases:"))
for i in range(t):
    a,b,c,d= map(int(input().split())
    if a-c > b-d:
        print("First")
    else:
        print("Second")
"""


# 12 ---> N students and x candies
"""
t=int(input())
for i in range(t):
    n,x= map(int,input().split())
    if n>x:
        k = n-x
        if k%4==0:
            print(k//4)
        else:
            print((k//4)+1)
    else:
        print(0)
"""


#13 ---> Find the number of pizza needed if no of persons and slices they eat are given and each pizza contain 4 slices
#Approach-1 -->using control statements
"""
t= int(input())
for i in range(t):
    n,s=map(int,input("no of people and slices they eat:").split())
    sl_req= n*s
    if(sl_req%4==0):
        print(sl_req//4)
    else:
        print((sl_req//4)+1)
"""

#Approach-2 --> using while(how a person thinks)
"""
t= int(input())
for i in range(t):
    n,s=map(int,input("no of people and slices they eat:").split())
    ts=n*s
    tp=0
    while ts>4:
        tp= tp+1
        ts=ts-4
    if ts==0:
        print(tp)
    else:
        print(tp+1)
"""



