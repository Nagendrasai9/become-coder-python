##a,b=map(int,input().split())
##print(a%b)



##a,b=map(int,input().split())
##print(a>b)




##a=input()
##b=input()
##print(ord('a')+ord('b'))





##r=int(input())
##perimeter =3.14*r*2
##area=3.14*r*r
##diameter=r*2
##print('perimeter:',perimeter,'area:',area,'diameter:',diameter)
##



##l=int(input())
##b=int(input())
##a=l*l+b*b
##print('area:',l*b)
##print('perimeter:',2*(l+b))
##print('diagnol:',a**(1/2))


 
##a=int(input())
##if not a%2:
##                print('even')
##else:
##                print('odd')



##a=int(input())
##if a>0:
##                print('positive')
##elif a==0:
##                print('zero')
##else:
##                print('negative')
##





##num=int(input())
##for i in range(num,-1,-1):
##                print(i,end=' ')




##num=int(input())
##while True:
##               if num==0:
##                               break
##               print(num,end=' ')
##               num-=1
                




##num=int(input())
##s=0
##def value(num):
##                while num:
##                                
##                   r=num%10
##                   num=num//10
##                   s+=r
##                   if s==0:
##                                   break
##print(s)



##a,b,c=map(int,input().split())
##if b<c:
##                x=b
##                y=c+1
##                d=1
##elif b>c:
##                x=c
##                y=b-1
##                d=-1
##for i in range(1,c+1):
##                if (a*i)%3==0:
##                                continue
##                print(a,'X',i,'=',a*i)
##
                                                



##num=int(input())
##ecount=0
##ocount=0
##x=0
##y=0
##while num:
##     r=num%10
##     num=num//10
##     if r%2==0:
##          x=x*10+r
##     else:
##          y=y*10+r
##print(x,'',y)          
##if ecount%2==0 and ocount%2!=0:
##     print('even   odd')
##elif ecount%2==0 and ocount%2==0:
##     print('even')
##elif ecount%2!=0 and ocount%2!=0:
##     print('odd')
##else:
##     print('mixed')



num,s,re=map(int,input().split())
count=0
x=0
while num:
     r=num%10
     num=num//10
     if r==s:
          r=re
     elif r%s==0:
          r=(r//s)
     x=x+r*pow(10,count)
     count+=1
print(x)
