

#list
a=[1211,'teja','yanagala',13]
print(a[1])
print(a[2])
print(a[3])
print(a[0])
print(a[-1])
a[0]=1200
print(a)
a[2]=5
print(a)
print(a[-3][-1])
print(a[:-3:-1])
print(a[:4:])
print(a.append(2))
print(a)
a.insert(4,'yr')
print(a)
a.extend([987,876])
print(a)
for i in a:
    print(i)


print(a)
a=[1,2,2,6532,56,'teja','yanagala']
a.clear()
a=[1,2,2,6532,56,'teja','yanagala']
a.clear()
print(a)
a.clear()
print(a)
a=[1,1,1,2]
b=[5,5,'teja']
c=a.append(b)
c=[]
print(a.append(b))

a=[1,2,3]
b=[78,86,4,654]
a.extend(b)
print(a)
c=a.copy()
print(c)
c.sort()
print(c)
d=[1,2,8965,]

print(sum(d))

a=[1,2,2,2,2,2]
b=['etah','teja','yanagala']
c=list([1,2,'tteja'])
print(a)
print(b)
print(c)
a.extend(b)
a.insert(2,'tyuuiyiyyuiy')

c.append(3)
print(a)
print(b)
print(c)
a.pop()
a.pop(3)
a.remove(2)

b.sort( )    
print(a)

a=[2,12,3,2]
a.reverse()
print(a)
a.count(2)
print(a.count(2))
v=a.copy()
print(v)
print(max(v))
print(min(v))
print(sum(v))
print(len(v)

r=(546,456,123,1)
print(r)
r[-1]
print(r[-1])
print(sum(r))
print(min(r))
print(max(r))
print(len(r))
print(sorted(r))
a=[999,888,777,444,555]
a.sort()
print(a.sort())
print(sorted(a))
print(r.count(1))
s=r.copy()
print(s)

a={1,11,'teja',11,1}
print(a)
a.add(222222222)
print(a)
a.update([432,324,324])
print(a)
print(a.pop())
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a)
a.pop()
print(a)

a={1,2,2,3.2}
a.update([12,321,456,'teja'])
b={456,2,654,'dwede'}
print(a)
a.remove(12)
print(a)
a.discard(321)
print(a)
print(b)
c=b.difference(a)
print(c)

a={"name":'teja',"age":22,"gender":'male'}
print(a.keys())
print(a.values())
print(a.get('name'))
print(a['name'])

a={101:'teja',102:'yanagala',103:'tejay'}
print(a.fromkeys([101,'teja']))

a=['teja',{101:'yanagala',102:'tejay',103:'tuo'},{1,2,3,4}]
print(a[-2][101])


a={101:'teja',102:'yanagala',103:'tejay'}
a1={105:'we',104:'wqaed'}
a.update(a1)
print(a)
print(sorted(a))
print(a)
a.pop(105)
print(a)
a.popitem()
print(a)
a.popitem()
print(a)
a.clear()
print(a)

a={'name':'teja',102:'yanagala',103:'tejay'}
for i in a[0,1]:
    print(i)

x=['apple','grape','orange']
new_list=[]
for i in x:
    if "a" in i:
        new_list.append(x)
print(new_list)

def name():
    print('hello world!')
name()

def name(j):
    print(j+" "+"is a good boy")
name("teja")
name("raju")
name("ramu")

def teja(fname,lname):
    print(fname+" "+lname)
teja("yanagala","teja")

def name(**arg):
    print("good boy is"+" "+arg['last'])
name(name1="teja",surname="yanagala",last="roy")

def rf(village="narasapuram"):
    print("i am from"+" "+village)
rf("ramabhadrapram")
rf("hyd")
rf()
rf("viz")
rf()

def fun(a):
    for x in a:
        print(x)
a=[123,321,456,654,789,987]
fun(a)


def name(x):
    return 5*x
print(name(1))
print(name(2))

x=lambda a,b:a*b
print(x(5,5))

def fun(n):
    return lambda a:a*n

b=fun(2)
print(b(11))


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("teja",22)
print(p1.name)
print(p1.age)




    def add(self,a,b):
        a=int(input())
        b=int(input())
        c=a+b
        return c

print(c)

    

def add(a,b):
    c=a+b
    return c
print(add(5,6))

def add(a,b):
    return a+b

c=int(input("enter"))
d=int(input("enter"))
add(c,d)
print(c+d)

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def child(self):
        print(self.fname,self.lname)
p1=Person("teja","roy")
p1.child()

a=56
txt="the cost of the is {}"
print(txt.format())















l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
l1.append(l2)
print(l1)


l1=[[1,2,3],(1,2,3),{'name':'teja','age':21},'pavan']
print(len(l1))
l1[0].append(4)
l1[2]['age']=22
l1[3]='pavana'+"kumar"
print(l1)


#t
for rows in range(6):
    for cols in range(6):
        #if (rows==0)or((rows==0 or rows==1 or rows==2 or rows==3 or rows==4 or rows==5 or rows==6 or rows==7) and(cols>4 and cols<6)):
        if ((rows==0) or (cols==5)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print('---------------------------------------------------------------------------------------------------------------------------------------------')

#s
for rows in range(7):
    for cols in range(7):
        if ((rows==0 or rows==3 or rows==6) or (cols==0 and rows!=4 and rows!=5 )or( cols==6 and rows!=1 and rows!=2)):
        #if ((rows!=1 and rows!=2 and rows!=4 and rows!=5 ) or (rows==0 and rows==3  and rows==6)or (cols==0 and rows!=4 and rows!=5) or (cols==6 and rows!=1 and rows!=2 )):
            print("*",end="")
        else:
            print(end=" ")
    print()
print('---------------------------------------------------------------------------------------------------------------------------------------------')

#e
for rows in range(7):
    for cols in range(7):
        if ((rows==0 or rows==3  or rows==6)or (cols==0  ) ):
            print("*",end="")
        else:
            print(end=" ")
    print()
print('---------------------------------------------------------------------------------------------------------------------------------------------')

#z
for rows in range(7):
    for cols in range(7):
        if ((rows==0 or rows==6) or(cols==6 or rows!=1 ) and (cols==5 or rows!=2) and (cols==4 or rows!=3) and (cols==3 or rows!=4) and(cols==2 or rows!=5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
print('---------------------------------------------------------------------------------------------------------------------------------------------')
#W
for rows in range(7):
    for cols in range(7):
        if ((cols==0 or cols==6)  or (cols==3 and rows==3) or (cols==1 and rows==5 or cols==5 and rows==5) or (cols==2 and rows==4 or cols==4 and rows==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print('---------------------------------------------------------------------------------------------------------------------------------------------')
#I
for rows in range(6):
    for cols in range(6):
        #if (rows==0)or((rows==0 or rows==1 or rows==2 or rows==3 or rows==4 or rows==5 or rows==6 or rows==7) and(cols>4 and cols<6)):
        if ((rows==0) or (cols==5 ) or(rows==5)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print('---------------------------------------------------------------------------------------------------------------------------------------------')
#B

#cal
def fun(x,y):
    pass
while True:
    a=int(input('enter first number :'))
    b=int(input('enter second number :'))
    print('---------------------------------')
    print('1.addition')
    print('2.subtraction')
    print('3.multiplation')
    print('4.division')
    print('5.exit')
    opt=int(input('enter any option'))
    print('-------------------------------------')
    if opt==1:
        c=fun(a,b)
        print(a+b)
        break
    elif opt==2:
        c=fun(a,b)
        print(a-b)
        break
    elif opt==3:
        c=fun(a,b)
        print(a*b)
        break
    elif opt==4:
        c=fun(a,b)
        print(a/b)
        break
    else:
        print('pls enter vaild data')

#cal
def cal(x,y,z):
    if z=='add':
        print(x+y)
    elif z=='sub':
        print(x-y)
    elif z=='mul':
        print(x*y)
    elif z=='div':
        print(x/y)
cal(4,5,z='sub')




#FUNCTION
def function():
    print('hello world')
function()

def function(fname):
    print(fname)
function("teja")

def function(fname,lname):
    print(fname,lname)
function("teja","yanagala")

def function(*arg):
    print('youngest amoung all',arg[1])
function("teja","raju","ramu")

def function(child1,child2,child3):
    print("older amoung all",child1)
function("teja","ramu","raju")

def function(**arg):
    print("older amoung all",arg['child2'])
function(child1="teja",child2="yanagala",child3="raju")

def function(*arg):
    print("older amoung all",arg[1])
function("teja",'raju',"a")

def function(**arg):
    print("older amoung all" ,arg["child1"])
function(child1="teja",child2="yanagala",child3="raju")

def function(country="india"):
    print("my country is:",country)
function("england")
function("aus")
function()
function("island")    

#new
def food(lis):
    for x in lis:
        print(x)
lis=["apple","banana","orange"]
food(lis)]

def number(n):
    pass
print(number(5))
print(number(6))
print(number(7))

#new
def trey(k):
    if (k>0):
        result=k+trey(k -1)
        print(result)
    else:
        result=0
    return result

print("\n\n example result")
trey(6)

#new
class Parent:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("hello my name is",self.name)
p1=Parent("teja")
p1.say_hi()

class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("hello my name is",self.name)
p1=Person("teja")
p2=Person("yanagala")
p3=Person("teha")

p1.say_hi()
p2.say_hi()
p3.say_hi()

#new
class A:
    def __init__(self,something):
        print('i am A')
        self.something=something
class B(A):
    def __init__(self,something):
        A.__init__(self,something)
        print("i am b")
obj=B('something')

class A:
    def __init__(self,something):
        print('i am A')
        self.something=something
class B(A):
    def __init__(self,something):
        print('i am b')
        A.__init__(self,something)
obj=B('something')

class Object:
    def __init__(self):
        print('address of self',id(self))
obj=Object()
print('address of class',id(obj))


class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('addition of two number',self.a+self.b)
z=Add(5,6)
z.add()

class Car():
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def modedl(self):
        print('model of the car:',self.model)
        print('color of the car:',self.color)
c1=Car('audi x3','red')
c2=Car('bmw 7t','white')
c1.modedl()
c2.modedl()

class First:
    def __init__(self):
        self.name='yanagala teja'
    def display(self):
        print(self.name)
f=First()
f.display()

class First:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        print("first number is",self.first)
        print("second number is",self.second)
        print("addition two number:",self.first+self.second)
f=First(1000,2000)
f.add()

class Employee:
    def __init__(self):
        self.name="teja"
        self.age=22
        self.comp="dvara"
e=Employee()
print("name of the employee:",e.name)
print("age of the employeee:",e.age)
print("comp of the employee:",e.comp)

class Emplyee:
    def __init__(self):
        self.name="teja"
        self.age=22
    def adsress(self):
        self.add='us'
e=Emplyee()
print(e.__dict__)
e.adsress()
print(e.__dict__)
e.emp_id=123
print(e.__dict__)

class Employee:
    def __init__(self):
        self.nam="teja"
        self.age=22
    def addr(self):
        self.add="us"
    
e=Employee()
print(e.__dict__)
e.addr()
print(e.__dict__)
del e.nam
print(e.__dict__)

class Employee():
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isEmployee(self):
        return False
class Person(Employee):
    def isEmployee(self):
        return True
e1=Employee("teja")
print(e1.getname(),e1.isEmployee())
e1=Person("yanagala")
print(e1.getname(),e1.isEmployee())
#single inheritance
class Employee():
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
class Person(Employee):
    def __init__(self,name,idno,sal,post):
        self.sal=sal
        self.post=post
        Employee.__init__(self,name,idno)
    def display(self):
        print(self.name,self.idno,self.sal,self.post)
        
e=Person("teja",87,75000,"SE")
e.display()

#multiple inheritance
class Base1():
    def __init__(self):
        self.name="teja"
        print("teja")
class Base2():
    def __init__(self):
        self.sname="yanagala"
        print("yanagala")
class Der(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("roy")
    def display(self):
        print(self.name,self.sname)
e=Der()
e.display()

#Multilevel inheritance
class Base():
    def __init__(self,name):
        self.name=name
    def gename(self):
        return self.name
class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age=age
    def geage(self):
        return self.age
class GrandChild(Child):
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address=address
    def geaddress(self):
        return self.address
g=GrandChild("teja",22,"narasapuram")
print(g.gename(),g.geage(),g.geaddress())


#private

class C():
    def __init__(self):
        self.a=45
        self.__d=56
    def display(self):
        print(self.__d)
class D(C):
    def __init__(self):
        C.__init__(self)
        self.e=85
        
v=D()
print(v.a,v.e)
q=C()
q.display()


#classmethods and static methos
from datetime import date
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthyear(cls,name,year):
        return cls(name,date.today().year-year)
    @staticmethod
    def isVaild(age):
        return age>=18
p1=Person("teja",21)
p2=Person.fromBirthyear("teja",2000)

print(p1.age)
print(p2.age)
print(p2.isVaild(21))


#accessing attributes
class Person():
    name="teja"
    sal='30000'
    def show(self):
        print(self.name)
        print(self.sal)
e=Person()
e.show()
print(getattr(e,'name'))
print(hasattr(e,'name'))
print(setattr(e,"age",22))
print(getattr(e,'age'))
print(delattr(e,'age'))
print(getattr(e,"age"))

#built-in attributes
class Person:
    'This all about accessing attributes'
    def __init__(self):
        print("this is __init__ method or constructor")
print(Person.__doc__)
print(Person.__name__)
print(Person.__base__)
print(Person.__dict__)
print(Person.__module__)


#RegEx
import re
t="name: yanagala teja"
match=re.search(r'teja',t)
print("starting index:",match.start())
print("ending indexing:",match.end())

import re
t="yanagala.teja"
match=re.search(r'.',t)
print(match)
match=re.search(r'\.',t)
print(match)

import re

match=re.compile('[e-v]')
a=match.findall("sdiorhskdodjssswertyuiolkjjmnvvcxsdrtyuiolk,nb zxsaqwertyklmnbv ")

import re
p=re.compile('\d')
print(p.findall("i was wake up at 11 A.M ON 2022"))
p=re.compile('\d+')
print(p.findall("i was wake up at 11 A.M ON 2022"))

#problems solveing
class Vehicle:
    def __init__(self):
        self.max_speed=50
        self.mileage=35
v=Vehicle()
print(v.max_speed,v.mileage)

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
v=Vehicle(240,25)
print(v.max_speed,v.mileage)
class Vehicle:
    pass

class Vechicle(object):
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
class Bus(Vechicle):
    def __init__(self,name,age,sal,id_no):
        Vechicle.__init__(self,age,name,age)
        self.id_no=id_no
b=Bus("teja",22,30000,2154)
print(b.name,b.age,b.sal,b.id_no)

#
class Vechicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vechicle):
    def __init__(self,name,max_speed,mileage,color="white"):
        Vechicle.__init__(self,name,max_speed,mileage)
        self.color=color
class Car(Vechicle):
    def __init__(self,name,max_speed,mileage,color="while"):
        Vechicle.__init__(self,name,max_speed,mileage)
        self.color=color
c=Car("audi Q5",240,18)
print(c.color,c.name,c.max_speed,c.mileage)
b=Bus("school volvo",180,12)
print(b.color,b.name,b.max_speed,b.mileage)

#
class Vechicle:
    color="white"
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vechicle):
    pass
class Car(Vechicle):
    pass
c=Car("AUDI Q5",240,18)
print(c.color,c.name,c.max_speed,c.mileage)
b=Bus("school volvo",180,12)
print(b.color,b.name,b.max_speed,b.mileage)

class Vechicle:
    def __init__(self,name,milieage,capacity):
        self.name=name
        self.milieage=milieage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100
class Bus(Vechicle):
    def fare(self):
        amount=super().fare()
        amount+=amount*10/100
        return amount
b=Bus("volvo",12,50)
print(b.fare())
        

def demo(name,age):
    print(name,age)
demo("teja",22)

def fun1(**args):
    for i in args:
        print(args)
fun1(name='teja',age=22)

def cal(a,b):
    return a+b,a-b
print(cal(40,10))

def cal(a,b,z):
    if z=='add':
        return a+b
    elif z=="sub":
        return a-b
    elif z=="mul":
        return a*b
    elif z=="div":
        return a/b
print(cal(25,5,z="add"))

#recursive
def addtition(num):
    if num:
        return num+addtition(num-1)
    else:
        return 0
r=addtition(15)
print(r)

def recursive_fun(x):
    addition = 0
    for i in range(1, x+1):
        addition = addition + i
    
    return addition
resu = recursive_fun(10)
print(resu)

import array
for i in array.__dict__:
    print(i)

#namespace==__dict__
class Student:
    def __init__(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
c=Student("teja",22,789645213)
print(c.__dict__)
#namespace=__dict__,__module__
class Teacher:
    def __init__(self,name,age,id_no):
        self.name=name
        self.age=age
        self.id_no=id_no
class Student(Teacher):
    def __init__(self,name,age,id_no):
        i=super().__init__()
        return i
c=Teacher("teja",22,789)
print(c.__dict__)
print(c.__module__)

file1=open("y.txt","w")
l=["this is hyd \n","this is narasapuram \n","this is london \n"]
file1.write("teja \n")
file1.writelines(l)
file1.close()
file1=open("y.txt","r+")
print("out of read function is")
print(file1.read())
print()

#lambda
letter=list(filter(lambda x:x,'human'))
print(letter)
#comprehension
letter=[x for x in range(20) if x%2==0]
print(letter)

l=[1,65,89956,45564,645,2]
n=list(map(lambda x: x*2, l))
print(n)

l=[32,23,233,222,32,12,23,34,101]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l[::-1)]

l=[2,23,3,3,33,32,213123,33]
l=list(dict.fromkeys(l))
print(l)

#NEW
class Student:
    def __init__(self):
        self.name="teja"
        self.id=98
    def display(self):
        print(self.name,self.id)
s=Student()
s.display()

s="teja yanagala"
s.split()
print(s.split())
print(s[1])
print(" ".join(reversed(s.split())))

l=[
i=0
for i in range(i,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=j
print(l)





#teja yanagala to yanagala teja
s="teja yanagala"
print(s)
print(s.split())


print(" ".join(reversed(s.split())))
print(s)

#new
class Rectanglee():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        return self.a*self.b
r=Rectanglee(5,4)

print(r.display())
 

#new
def add(datatype,*arg):
    if datatype=='int':
        answer=0
    if datatype=='str':
        answer=''
    for x in arg:
        answer=answer+x
    print(answer)
add("int",5,6)
add("str","hi ", "teja")

#new
class A:
    def show(self):
        print("I am a class")
class B(A):
    def show(self):
        super().show()
        print("I am b class")
a=B()
a.show()


#excepations
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError as x:
    print(x)
else:
    print("program success")
finally:
    print("thank you")

import random as r
#print(r.randint(1,9))

x=[1,2,3,4]
r.shuffle(x)
print(x)

print(r.randint(1,9),r.randint(1,9),r.randint(1,9),r.randint(1,9))

for i in range(4):
    print(r.randint(1,9),end=" ")
#new






rr = [5, 2, 8, 7, 1];     
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
#Sort the array in ascending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");




class Add:
    def add(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b

    def display(self,a,b):
        Add.add(self,a,b)
        print(self.c)
x=Add()
x.display(5,5)

#ascending order without built-in-function
l=[0,5,4,2,11,13,17,14,12,8,7,19,22,20]
i=0
for i in range(i,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(l)


#swapping
#method1
#i/p=[34,1,3,43]
#o/p=[43,1,3,34]
def Swap(newlist):
    size=len(newlist)

    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[34,1,3,43]
print(Swap(newlist))

#method2
#i/p=[34,1,3,43]
#o/p=[43,1,3,34]
def swap(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist
newlist=[34,1,3,43]
print(swap(newlist))


#i/p=[34,1,3,43]
#o/p=[3,1,34,43]
newlist=[34,1,3,43]
def swap(newlist):
    newlist[0],newlist[-2]=newlist[-2],newlist[0]
    return newlist
print(swap(newlist))


#find the length of list
l=[34,1,3,43]
count=0
for i in l:
    count+=1
print(count)


#revesing the list
l=[34,1,3,43]
print(l[::-1])
print(sum(l))

total=0
ne=[1,2,3,4]

for i in range(0,len(ne)):
    total=total+ne[i]
print(total)
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------

#reveseing of list
a=[1,2,3,4,5,6,7,8,9,10]
print(a[::-1])

#Concatenate two lists index-wise
a=["m","na","te","yana"]
b=["y","me","ja","gala"]
c=[a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]
print(c)


#Turn every item of a list into its square
a=[1,2,3,4,5,6,7,8,9]
b=[x*x for x in a]
print(b)

# Concatenate two lists in the following order
a=["hello","take"]
b=["dear","sir"]
c=[a[0]+b[1],a[1]+b[1],a[1]+b[0]]
print(c)

#Iterate both lists simultaneously
a=[10,20,30,40]
b=[100,200,300,400]
for a,b in zip(a,b[::-1]):
    print(a,b)
    
#Remove empty strings from the list of strings
a=["teja","","yanagala","roy"]
b=list(filter(None,a))
print(b)

#Add new item to list after a specified item
#[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#a = [10, 20, [300, 400, [5000, 6000,7000], 500], 30, 40]
a = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
a[2][2].append(7000)
print(a)

#opening n reading file
f=open('E:\sample of open file.txt')
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
line4=f.readline()
print(line4)
f.close()


#new
f=open("E:\sample of open file.txt")
while True:
    try:
        line=next(f)
        print(line)
    except StopIteration:
        break
f.close()


#access all lines by using loops
f=open("E:\sample of open file.txt")
for i in f:
    print(i)


f=open("E:\sample of open file.txt",'r')
for i in f:
    print(i)

f=open("E:\sample of open file.txt","w")
f.write("yanagala teja")
f.close()

#read
f=open("E:\sample of open file.txt","r")
for i in f:
    print(i)

#read
f=open("E:\sample of open file.txt","r")
for i in f:
    print(i)

f=open("E:\sample of open file.txt","r")
for i in f:
    print(i)
f.close()
#write
f=open("E:\sample of open file.txt","w")
f.write("yanagala te")
f.close

#read
f=open("E:\sample of open file.txt","r")
for i in f:
    print(i)
f.close()

f=open("E:\sample of open file.txt","a")
f.write("j")
    f.close

f=open("E:\sample of open file.txt","a")
f.write("roy")

f=open("E:\sample of open file.txt","r")
print(f.read())

s=(100,200,300)
print('{0}'.format(s))


=============================================================================================================================================================================================
                                ||mysql||
============================================================================================================================================================================================

#importing mysql and connecting to the python
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="205101tejaT@"
    )
print(mydb)

#creating a database
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE teja")

#to check the database or print the database
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword"
    )
mycurser=mydb.curser()
mycursor.execute("SHOW DATABASE")
for i in mycursor:
    print(i)

#Try connecting to the database "mydatabase":
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword",
    database="mydatabase"
    )

l=[65,1,78,23,0,1,3,78,5]
i=0
for i in range(i,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)


class Create(object):
    bal=1000
    def __init__(self,acc,name='teaj'):
        self.accno=3513214556
        self.name='teja'
        self.bal=1000
class Deposit():
    def deposit(self,dept,bal=1000):
        
        self.dept=dept
        self.bal=1000
d=Deposit()
d.deposit(5000)
print(d.dept+d.bal)
class Withdraw(Deposit):
    def withidraw(self,wt):
        self.wt=wt
        wt=int(input("enter withdraw amount"))
    





class Teache
    def __init__(self,name,age,id_no):
        self.name=name
        self.age=age
        self.id_no=id_no
class Student(Teacher):
    def __init__(self,name,age,id_no):
        i=super().__init__()
        return i
c=Teacher("teja",22,789)
print(c.__dict__)
print(c.__module__)

class Account:
    def __

import datetime
from datetime import date
date=str(input(" "))
day,month,year=date.split()
day_name=datetime.date(int(year),int(month),int(date))
print(day_name.strftime("%A"))


#input as date and output as day
import datetime as db
def day(x,y,z):
    c=db.date(x,y,z)
    e=c.strftime('%A')
    print(e)
z=day(2000,1,29)




                 
#smallest number among list
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]<l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(z)
    
   o/p:2
    
#lastest number among list
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(z)
    
    o/p:552


#ascending order
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(l)

o/p:[2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 17, 19, 20, 27, 552]

    


#decendind order
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]<l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(l)

o/p:[552, 27, 20, 19, 17, 14, 13, 12, 11, 10, 8, 7, 5, 4, 2]



























































