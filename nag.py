##class personal:
##    def __init__(self,name,adhar):
##        self.name=name
##        self.adhar=adhar
##    def display_data(self):
##        print(self.name,self.adhar)




##
##class student(personal):
##    college='aditya'
##    def __init__(self,rollno,per,name,adhar):
##        self.roll=rollno
##        self.per=per
##        super().__init__(name,adhar)
##    def display_data(self):
##        print(self.roll,self.per,self.college,)
##        super().display_data()
##    @classmethod
##    def classmethod(cls):
##        print(cls.college)
##    @staticmethod
##    def findgrade(per):
##        if per>75:
##            return 'A'
##s1=student(188,76,'nag',1213244)
##s1.display_data()
##s1.grade=s1.findgrade(s1.per)
##print(s1.grade)


##
##class personal:
##    def __init__(self,name,adhar):
##        self.name=name
##        self.adhar=adhar
##    def display_data(self):
##        print(self.name,self.adhar)
##class student(personal):
##    def __init__(self,roll,branch,name,adhar):
##        self.roll=roll
##        self.branch=branch
##        super().__init__(name,adhar)
##    def display_data(self):
##        print(self.roll,self.branch)
##        super().display_data()
##s1=student(11,'ece','nag',80580800099)
##s1.display_data()
##


##a=int(input())
##b=int(input())
##try:
##    res=a//b
##    print(res)
##except ZeroDivisionError:
##    print("zerodivision")
##except NameError:
##    print("name error")
##except:
##    print('error')
##finally:
##    print('something')

##def fun(n):
##    
##    if n<=0:
##        return 1
##    return n+fun(fun(n-2)-1)
##    
##n=5
##fun(n)


















##n=int(input())
##k=int(input())
##x=0
##y=0
##if n<k:
##   for i in range(n,k+1):
##      if i%2==0:
##        x+=i
##      else:
##        y+=i
##      
##   print(x,y)
##elif n>k:
##    n,k=k,n
##    for i in range(n,k+1):
##      if i%2==0:
##        x+=i
##      else:
##        y+=i
##    print(x,y)
##    
##    
##    
##



##
##n=int(input())
##x=0
##while n:
##   r=n%10
##   x=x*10+r
##   n=n//10
##print(x)

##
##a=list(map(int,input().split()))
##b=set(a)
##d={}
##for i in b:
##   d[i]=a.count(i)
##print(d)
##   
##   

##
##class stack:
##    def __init__(self,size,d=[]):
##        self.size=size
##        self.data=d
##    def push(self,val):
##        if len(self.data)==self.size:
##            print("stack is full")
##        else:
##            self.data.append(val)
##    def pop(self):
##        if len(self.data)==0:
##            print("stack is empty")
##        else:
##            return self.data.pop()
##    def get_max_size(self):
##        return self.size
##    def is_empty(self):
##        return len(self.data)==0
##
##
##input_stack=stack(5,[1,2,3,4,5])






##def fun(input_stack):
##    num = input_stack.4
##    while(num > 0):
##        top_element = input_stack.pop()
##        temp_stack = Stack(input_stack.get_max_size())
##        element = input_stack.pop()
##        temp_stack.push(element + top_element)
##        if(not temp_stack.is_empty()):
##            if(not input_stack.is_empty()):
##                input_stack.push(temp_stack.pop()+input_stack.pop())
##            else:
##                input_stack.push(temp_stack.pop())
##        input_stack.push(top_element)
##        num -= 1
##    return input_stack
##input_stack=[8,7,3,4,5]
##print(fun(input_stack))


##from math import sqrt
##def isprime(n):
##    
##    
##    if n>1:
##      for i in range(2,n//2+1):
##        if n%i==0:
##            return False
##        else:
##            return True
##    else:
##        return False
##        
##n=int(input())
##k,m=0,0
##i,j=1,1
##while True:
##    if n%2==0:
##        if isprime(n-i):
##            k=n-i
##            if isprime(n+j):
##                m=n+j
##                break
##        i+=1
##        
##    else:
##        j+=2
##print(k,m)
##
##
##    
        
##        
##def reverse(n):
##    x=0
##    while n:
##        r=n%10
##        n=n//10
##        x=x*10+r
##    return x
##n=int(input())
##if n==reverse(n):
##    print(n)
##else:
##    i=1
##    while True:
##        if n-i==reverse(n-i):
##            L=n-i
##            break
##        i+=1
##    i=1
##    while True:
##        if n+i==reverse(n+i):
##            R=n+i
##            break
##        i+=1
##if abs(n-L)>abs(n-R):
##    print(L)
##elif abs(n-L)==abs(n-R):
##    print(L,R)
##else:
##    print(R)


##
##a,b=list(map(int,input().split()))
##t=2
##x=1
##while True:
##    if a%t==0 and b%t==0:
##        a=a//t
##        b=b//t
##        x=x*t
##    else:
##        t+=1
##        if a<t or b<t:
##            break
##print(x*a*b)
##
##
##



##def lcm(a,b,t=2):
##    if a<t or b<t:
##        return a*b
##    if a%t==0 and b%t==0:
##        return t*lcm(a//t,b//t,t)
##    else:
##        return 1*lcm(a,b,t+1)
##
##a,b=map(int,input().split())
##print(lcm(a,b))
##
##



##def gcd(a,b):
##    if b==0:
##        return a
##    if a>b:
##        a,b=b,a
##    return gcd(a,b%a)
##
####a,b=map(int,input().split())
####print(gcd(a,b))
##
##
###n=int(input())
##d=list(map(int,input().split()))
##x=d[0]
##for i in d[1:]:
##    x=gcd(x,i)
##print(x)



##n=int(input())
##k=list(map(int,input().split()))
##s=""
##for i in k:
##    s+=str(i)
##print(s)

##for i in range(1):
##
##        print("#")
##
##else:
##
##        print("#")

##i = 1
##while True:
##    if i%3 == 0:
##        break
##    print(i)
## 
##    i += 1

##
##i=1
##while(i<6):
##    j=0
##    while(j<3):
##        print(i%3,end=" ")
##        j=j+1
##    i=i+1
##


##tup = [1, 2, 4, 8]
##
##tup = tup[-2:-1]
##
##tup = tup[-1]
##
##print(tup)
##

##
##x = 0
##a = 5
##b = 5
##if a > 0:
##    if b < 0: 
##        x = x + 5 
##    elif a > 5:
##        x = x + 4
##    else:
##        x = x + 3
##else:
##    x = x + 2
##print(x)


##
##str1 = "My salary is 7000";
##str2 = "7000"
##
##print(str1.isdigit())
##print(str2.isdigit())
##
##

##example="helloworld"
##print(example[::-1].startswith("d"))
##

##
##from itertools import permutations
##def isprime(n):
##    if n>1:
##        for i in range(2,n):
##            if n%i==0:
##                return False
##    else:
##        False
##
##data=input()
##data=list(data)
##d=[]
##x=[]
##for i in data:
##    d.append(str(ord(i)))
##p=list(permutations(d,3))
##for j in p:
##    s=""
##    for i in s:
##        s=s+i
##    m=int(s)
##    if isprime(m):
##        x.append(m)
##print(m)
##        
##



##
##s1=input()
##s2=input()
##s1=s1.lower()
##s2=s2.lower()
##k=[]
##s=""
##for i in s1:
##    if i in s2:
##        k.append(i)
##m=sorted(k)
##n=list(set(m))
##p=sorted(n)
##p.remove(" ")
##x="".join(p)
##print(x)


##
##s=input()
##s=s.lower()
##k=[]
##for i in s:
##    if s.count(i)==1:
##        k.append(i)
##m=sorted(k)
##n="".join(m)
##print(n)


##
##s=input()
##k=list(s.split(" "))
##for i in k:
##    for 
##        

##
##a,b=map(int,input().split())
##k=[]
##m=[]
##for i in range(a):
##    p=list(map(int,input().split()))
##    k.append(p)
##    m.append(sum(p))
###print(m)
##c=0
##for i in range(b):
##    c+=k[j][i]

##print(c)
##
##





##
##
##a,b=map(int,input().split())
##k=[]
##m=[]
##for i in range(a):
##    p=list(map(int,input().split()))
##    k.append(p)
##    m.append(sum(p))
##
##for i in range(b):
##    c+=k[i][i]
##for i in range(a):
##    for j in range(a):
##        if i==a-j-1:
##            d+=k[i][j]
##            
##print(c,d)











##
##a,b=map(int,input().split())
##k=[]
##
##c=0
##for i in range(a):
##    p=list(map(int,input().split()))
##    k.append(p)
##m=k[:][:]
##print(m)
##for i in range(a):
##    for j in range(a):
##        k[i][j]=m[j][i]
##       
##print(m)




##a,b=map(int,input().split())
##k=[]
##
##c=0
##for i in range(a):
##    p=list(map(int,input().split()))
##    k.append(p)
##m=k
##print(m)
##for i in range(a):
##    for j in range(a):
##        k[i][j]=m[j][i]
##       
##print(m)
##
##
##









##
##
##
##
##a,b=map(int,input().split())
##k=[]
##m=[]
##for i in range(a):
##    p=list(map(int,input().split()))
##    k.append(p)
##    m.append(sum(p))
##
##for i in range(b):
##    c+=k[i][i]
##for i in range(a):
##    for j in range(a):
##        if i==a-j-1:
##            d+=k[i][j]
##            
##print(c,d)
##

##
##
##n=int(input())
##a,b=0,1
##x=0
##if n==1:
##    print('0')
##else:
##    while x<n:
##        print(a,end=" ")
##        k=a+b
##        
##        a=b
##        b=k
##        x+=1
        
    
##a,b=map(int,input().split())
##g,lcm=0,0
##if a>b:
##    g=a
##else:
##    g=b
##while True:
##    if (g%a==0) and (g%b==0):
##        lcm=g
##        break
##    g+=1
##print(lcm)
##        
##


a,b=map(int,input().split())
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        g=i
    i+=1
print(g)

















