'''
l=[2,34,64,84,246,2,557,457,4567]
for i in l:
    print(l)
 
    
x = list()
for i in range(1,15):
    x.append(i)
print(x)


import datetime as db
c=db.date(2000,5,2)
d=strftime(c)
print(d)

#input as date and output as day
import datetime as db
def day(x,y,z):
    c=db.date(x,y,z)
    e=c.strftime('%A')
    print(e)
z=day(2000,1,29)

d={'empid':1,'gross':'5k'}
d1={'empid':1,'net':'2k'}
d1=d.copy()
print(d1)

def s1(x):
    b = x.copy()
    l = set(x)
    m = 0
    h = dict()
    for i in l:
        for j in b:
            if i == j:
                m = m + 1
        q = {i: m}
        h.update(q)
        m = 0
    print(h)


l = [2, 1, 1, 5, 6, 5, 1, 3, 4, 1, 2, 1]
s1(l)





l=[{'empid:1','gross:5k'},{'empid:1','net:2k'},{'empid:1','pay:6k'},{'empid:2','gross:3k'},{'empid:3','gross:5k'},{'empid:3','net:3k'},{'empid:4','pay:3k'}]
l1=[]
l2={}
for i in l:
    l2.update(i)   
print(l2)



s={}
for i in l:
    s.update(i)
print(s)
'''

'''
l1 =for x in l
a=[]
a.append(l1)
print(a)
l1={}

print(l1)
for i in l:
    l1.update(i)
print(l1)

    
l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'5k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
s=set()
q=[]
#q.append()
for keys,values in l:
    s.add(keys)
print(s)

def s1(x):
    b = x.copy()
    l = set(x)
    m = 0
    h = dict()
    for i in l:
        for j in b:
            if i == j:
                m = m + 1
        q = {i: m}
        h.update(q)
        m = 0
    print(h)


l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'5k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
s1(l)

l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'5k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
#l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'5k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
s=set()
q=[]
#q.append()
for keys,values in l:
    print(values)

l=[{'empid1':1,'gross1':'5k'},{'empid1':1,'net1':'2k'},{'empid1':1,'pay1':'6k'},{'empid2':2,'gross2':'3k'},{'empid3':3,'gross2':'7k'},{'empid3':3,'net3':'3k'},{'empid4':4,'pay4':'3k'}]
s={}
q=[]
for i in l: 
    s.update(i)
q.append(s)
print(q)

#adding of two dict
dict_1 = {'empid':1 ,'gross':'5k'}
dict_2 = {'empid':1,'net':'3k'}
dict_3={'empid':2,'gross':4000}
dict_4={'empid':2,'net':'5k'}


print([{**dict_1,**dict_2},{**dict_3,**dict_4}])

l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'7k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
print([{**l[0],**l[1],**l[2]},{**l[3]},{**l[4],**l[5]},{**l[6]}])

l=[{'empid':1,'gross':'5k'},{'empid':1,'net':'2k'},{'empid':1,'pay':'6k'},{'empid':2,'gross':'3k'},{'empid':3,'gross':'7k'},{'empid':3,'net':'3k'},{'empid':4,'pay':'3k'}]
print([{**l[0],**l[1],**l[2]},{**l[3]},{**l[4],**l[5]},{**l[6]}])

n=int(input('enter any value'))
for i in  range(20):
    s=n*i
    print(n,'*',i,'=',s)


n=int(input('enter any valure'))
l=[1,2,3,78,56]
for i in l:
    if (i==n):
        print('yes given input is thier in list')
        break
else:
    print('invilad input')

s='teja'
s1='yanagala'
print(s+s1)

n=int(input('enter nth number'))
for i in range(10):
    s=n*i
    print(s)
'''


