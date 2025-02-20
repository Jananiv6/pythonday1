# Data Types

# int

a=50
print(a)
print(type(a))


b=25
print(b)
print(type(b))

# float

c=20.5
print(c)
print(type(c))

d=23.5
print(d)
print(type(d))

# Complex Numbers

e=6+7J
print(e)
print(type(e))

f=200+1J
print(f)
print(type(f))

# Boolean

g=True 
print(g)
print(type(g))

h=False 
print(h)
print(type(h))

# String

i="Janani"
print(i)
print(type(i))

j="janu"
print(j)
print(type(j))

# List

k=[6,7,1,"Janani","v"]
print(k)
print(type(k))

l=[23,7,"Janu","Janvi"]
print(l)
print(type(l))

# Tuple

m=(200,1,True,"Jan")
print(m)
print(type(m))

n=(2,14,"Bro")
print(n)
print(type(n))


# Set

o={29,"R","python"}
print(o)
print(type(o))

p={12,19,6,12,20,24,22,10}
print(p)
print(type(p))

# Range
q=range (23)
print(q)
print(type(q))

r=range (9)
print(r)
print(type(r))


# Dictionary 

s={1:"Janani",2:"Naveena"}
print(s)
print(type(s))

t={1:"R",29:"Python"}
print(t)
print(type(t))

# Operators

print("Arithmetic Operators")

u=23
v=5
print(u+v)
print(u-v)
print(u*v)
print(u/v)
print(u**v)
print(u%v)
print(u//v)

print("Relational Operators")

w=8
x=4
print(w==x)
print(w!=x)
print(w>=x)
print(w<=x)
print(w>x)
print(w<x)

print("Assignment Operators")

num=6
print(num)
num+=7
print(num)
num-=5
print(num)
num*=2
print(num)
num/=3
print(num)
num%=2
print(num)

print("Logical Operators")

y=6
z=7
print(y and z)
print(y or z)
print(not True)
print(not False)

print("Bitwise Operators")

ab=20
bc=1
print(ab & bc)
print(ab | bc)
print(ab ^ bc)
print(ab >> bc)
print(ab << bc)
print(~ bc)

print("Conditional Stmts")

# if
num1=5
if num>=0:
    print("+ve")


# if else
val1=7
if val1>9:
    print("+ve")
else:
    print("-ve")    

# elif
val2=9
if val1>7:
    print("Number Accepted")
elif val2==9:
    print("Ture")     

print("loops")

# for

for i in range(0,10):
    print(i)

num2=10  
num3=20
while num2>num3:
    print("True")
print("False")  


print("functions")

Name="Janani"
Nickname="Janu"
def name(Name,Nickname):
    print(Name,Nickname)


name(Name,Nickname)


def num():
    for j in range(0,10):
        if j%3==0:
            print(j)
            

num()           

print("Builtin functions")

dic = dict(name = "Janani", age = 23, country = "India")

print(dic)

As = ascii("My name is jånåni")
 
 
print(As)

