'''a=[1,1,1,1,5]
print(type(a))
print(a)
a=(1,1,11,1,2)
print(type(a))
print(a)
a={1,2,1}
print(a)

a=int(input('enter the bin number:'))
if a//10==0 and a%10:
    print('it is bin number')
else:
    print('it is not bin number')
'''

import sqlite3
conn=sqlite3.connect('teja55.db')
conn.execute("create table emp(empno int,ename varchar(20),sal float)")
print('yable create successfully...')

