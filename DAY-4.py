#p1 --> Pangrams hackerrank
#Approach-1 using sets(A-Z,a-z)
'''
str=input()
s={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
for i in str:
    if s[i] in str:
        print("Pangram")
    else:
        print("Not pangram")
'''
#Approach-2 add the string to set and if count of set==27 or >= 27 then it is pangram

#Approach-3 using dictionary(take only alphabets(exclude spaces,num,chars) into dict and if count of dict==26 then it is pangram)

# Approach-4 using list

#p2 ---> First repeating character(Hackerrank)
#Approach-1 ---> add str to dict and their values(their occurance) and iterate the dict for first value>=2
'''
t=int(input("Enter the test cases: "))
str=input()
'''


#p3 --> Dict and map(Hackerrank)
'''
n=int(input("Enter the no of names and phno: "))
d={}
for i in range(n):
    name,phno=input("Enter the name and phno: ").split()
    d[name]=phno
while True: # runs infinitely( to overcome use try else block)
    x=input("Enter the name: ")
    if x in d:
       print(x ,"=" ,d[x])
    else:
       print("Not found")
'''


#p4 -->Maximum word frequency (Eolymp)
'''
n=int(input("Enter the no of words: "))
dict={}
for i in range(n):
    words=input()
    for j in words:
       if j in dict:
           dict[j]+=1
       else:
           dict[j]=1
print(dict)
max_num=max(dict.values())
print(max_num)
l=[]
for k in dict:
    if max_num==dict[k]:
        l.append(k)
print(l)
print(max(l),max_num)
'''


#p5 Database (SPOJ-RPLD)


#P6 Implement graphs (directed,unweighted) using dict
'''
n=int(input("Enter the no of routes: "))
d={}
for i in range(n):
    city=input("Enter the city: ")
    nd=int(input("Enter the no of destinations"))
    for j in range(nd):
        dest=input("Enter the dest: ")
    d[cities]=dest
print(d)
'''


#p7 Implement graphs(directed,weighted)