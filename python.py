#def ex(a,b,c=23):
              #  return(a+b)
#a=int(input())
#b=int(input())
#print(ex(a,b))



              
def add(a,b):
                return(a+b)
def sub(a,b):
                return(a-b)
def mul(a,b):
                return(a*b)
def div(a,b):
                return(a//b)

a= int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
x=input('enter an operator:')

if x == '+':
    print(a+b)

elif x == '-':
    print(a-b)

elif x == '*':
    print(a*b)

elif x == '/':
    print(a/b)
else:
    print('cant perform this operation ')            

