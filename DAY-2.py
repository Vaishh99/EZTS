# Example for pass by refernce in python
'''
def fun(x):
    x[0]=20
lst = [10,11,12,13,14,15]
fun(lst)
lst[0]=100
print(lst)
'''


#p1 --> Sugarcane-codechef
#Approach-1 ---> with test case and using function for profit
'''
t=int(input("Enter the no of test cases: "))
for i in range(t):
    def profit(n):
      total= n*50
      exp= (0.7)* (n*50)
      profit= (total-exp)
      print(int(profit))
    x=int(input("Enter the no of glasses: "))
    profit(x)
'''

#Approach-2 ---> With functions for both profit and test case and return type for profit(to do)
'''
t=int(input())
def profit(n):
'''


# p2 movie at 2x speed -codechef(to do)
'''
t=int(input())
for i in range(t):
    total 
'''


#p3 --> count the number of 4's in an integer
#Approach-1 without any function
'''
t=int(input("Enter the test cases: "))
for i in range(t): 
    n=int(input("Enter the number: "))
    c=0
    while n>0:
        if n%10 == 4:
            c=c+1
        n= n//10
    print(c)
'''
#Approach-2 with recursive function(to do)
'''
t=int(input("Enter the test cases: "))
for i in range(t):
    def count(n):
        if n==0:
            return
        else:
'''

#p4 calculate N!
#Approach-1 general
'''
t=int(input())
while t>0:
    def fact(n):
       if n==1:
           return 1
       else:
           return(n*fact(n-1))
    fact(4)
'''

#p4 ---> Add 3 in front and back
'''
# Approach-1 divide by 1000 then we get decimal and add 3(added at beginning), now multiply by 1000 to get rid of decimal, noe multiply by 10 and add 3
# only possible if 3 digit number is given  (to do)
x=int(input())
y= (x*10) + 3
print(y)
for i in range(y):
    y=
'''
'''
#Approach-2 Using reverse
def reverse(x):
    if x>0:
        x%10 == 
x=int(input())
x=(x*10) + 3
print(x)
#reverse the number
'''