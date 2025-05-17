'''
st= 'aabbbaacdddbb'
count = 1
sub= ''
for i in range(len(st)-1):
    if st[i]==st[i+1]:
        count+=1
    else:
        sub += str(count)+st[i]
        count = 1
sub += str(count)+st[-1]
print(sub)
'''
# import time

'''
# longest substring without repeatation
st = 'abccbdabcde'
value= 0
count= 1
sub= ''
for i in range(len(st)-1):
    if st[i] == st[i+1]:
        pass
    else:
        sub+=st[i]
print(sub)
 '''

'''
n= 1
while(n<=10):
    print(n)
    n+=1
'''

'''
num = 1
sum = 0
while(num<=10):
    sum+=num
    num+=1
print(sum)
'''

'''
st = 'python'
ss= len(st)-1
new_ss= ''
while (ss>=0):
    new_ss+=st[ss]
    ss-=1
print(new_ss)
'''

'''
st= 'programing mania'
ss= len(st)-1
count= 0
while (ss>0):
    if st[ss] in 'aeiouAEIOU':
        count+=1
    ss-=1
print(count)
'''

# # Count the length
# st = 'python project'
# count = 0
#
# while(st!=''):
#     count+=1
#
# print(count)
# x=[]
# for i in range(1,6):
#     x.append(i*2)
# print(x)
'''
def odd(func):
    def list_odd(li):
        return [i for i in li if i % 2 == 0], func(li)
    return list_odd
@odd
def list_even(li):
    sum = 0
    for i in li:
        sum+=i
    return sum
li = [10,34,23,45,75,24,64]
print(list_even(li))
'''

'''
def dec(func):
    def old(li):
        word=[]
        for i in li:
            if type(i)==str:
                if i.isalpha():
                    word.append(i.capitalize())
        return word, func(li)
    return old
@dec
def new_li(li):
    res = 0
    for i in li:
        if type(i)==int:
            res+=i
    return res
li = [10,20,'78','querty', 90, '900', 'ctc']
print(new_li(li))
'''


'''
def dec_div(func):
    def div(a,b):
        res= a//2,b//2
        return res
    return div

def dec_cube(func):
    def cube(a,b):
        res= a**3+b**3
        return res, func(a,b)
    return cube

@dec_div
@dec_cube
def sqr(a,b):
    res= a**2+b**2
    return res
print(sqr(10,20))
'''

'''
def loop(digits):
    for i in digits:
        yield i

obj = loop([10,20,30])
for i in obj:
    print(i)
'''

'''important module.
MATH, OS, SYS, TIME, DATE, RANDOM, ABC, FAKER, SUBPROCESS'''


'''def armstrong(num,p):
    if num==0:
        return 0
    return (num%10)**p+armstrong(num//10,p)
num= int(input('Enter your number: '))
if num==armstrong(num,len(str(num))):
    print('Armstrong number')
else:
    print('Not armstrong')'''


'''import test
print(time.time())'''


'''import mysql.connector
conn= mysql.connector.connect(
    host= '127.0.0.1',
    port = '3306',
    user= 'root',
    password = 'RituMunu@123',
    database= 'AT18'
)

if conn.is_connected():
    print('Connected')
else:
    print('Not connected')'''