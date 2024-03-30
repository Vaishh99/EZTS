#p1 --> Find duplicate (Hackerrank)
#Approach-1 --> using membership
'''
x=int(input("Enter the number of elements: "))
l=list(map(int,input().split())) [:x]    #slices the string upto the given no.of elements
for i in range(x):
    if l[i] in l[i+1:]:
        print(l[i])
        break
'''

#Approach-2 --> Sort and then 2 pointer technique
'''
n=int(input("Enter the no.of elements: "))
l=list(map(int,input().split())) [:n]
print(l)
l.sort()
print(l)
for i in range(n-1):
    if l[i] == l[i+1]:
        print(l[i])
        break
'''

#Approach-3 --> Using count() method


#p2 --> unique elements in array (Hackerrank)
#Approach-1 --> using membership and another list to add the values  ( cannot find more thana 1 unique values correctly as the list checks from i+1 pos where it may have in the before sublist)
n=int(input("Enter the number of elements: "))
a=list(map(int,input().split())) [:n]
lst2=[]
for i in range(n):
    if (a[i] not in a[i+1:]):
        lst2.append(a[i])
print(lst2)

# Approach-2 --> count method (if count==1 then return the element)

#p3 --> Gravity flip (codeforces)
#Approach-1 sort method

#p4 --> Chef team (Codechef)
#Approach-1 --> list
'''
t= int(input())
for i in range(t):
    divisor = []
    n=int(input())
    for j in range(1,n+1):
        if n % j == 0:
            divisor.append(j)
    print(divisor)
'''

#Approach-2 --> Brute force


#p5 --> cost of groceries(Codechef) -kitchencost
'''
n,x= map(int,input("Enter the n and x values(number n min freshness): ").split())
l1=list(map(int,input("Freshness of n items:").split())) [:n]
l2=list(map(int,input("Cost of n items: ").split())) [:n]
print(l1)
print(l2)
cost=0
for i in range(n):
    if l1[i]>=x:
        cost = cost+ l2[i]
print(cost)
'''

#p6 --> Prime or not
# Approach-1 --> using factors and list(brute force)
'''
t=int(input("Enter the no of test cases: "))
for i in range(t):
    n=int(input("Enter the number: "))
    factors=[]
    for j in range(1,n+1):
        if n % j ==0:
            factors.append(j)
    print(factors)
    if len(factors)==2:
        print("prime")
    else:
        print("Not prime")
'''

# Approach-2 --> optimised and found on web( using flag,__)

#p7 Alice and bob (Codechef)(calculate how many days they were happy and unhappy)
'''
n=int(input("Enter the no of days: "))
for i in range(n):
    a=list(map(int,input("Alice distance in meters:").split()))
'''
#perfect
#palindrome
#amstrong

#p8 Even perfect number
#Approach-1 --> list

#Approach-2 --> more efficient
