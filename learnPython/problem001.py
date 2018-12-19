# 对于print的使用，换行符，字符串，字符串可以有两种表现形式
# 多行输出形式如下
print('hello')
print("I'm \"OK\"")
print('''fd
      fdf
      test
      df''')

# and or not 的bool值运算
print(True and False)
print(True or False)

# 条件判断
if(not 8>1):
    print("you")
else:
    print("hhhha")

# python可以随意定义变量
a = 1
print(a)
t_003 = "你知道我是谁吗"
print(t_003)

# 在算术运算之前如果是数字那么就可以使用，否则就回报错
a=123
print(a+23)

a='ASB'
print(a+"13")

a=123
a='BSc'
a=234
print(a+23)

# 除法跟整除
print(10/3)
print(10//3)

# python 在内存中把字符串当作Unicode表示
x='ABC'
print(x.encode('utf-8'))   # 输出  b'ABC'
# 如果出错，则忽略，通过decode把十六进制转化一下
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 占位符  %d  %f  %s  %x  整数  浮点数 字符串 十六进制
print('hello %s' % 'world')


# List 是一种有序集合，可以随时添加元素
classmates = ['Michael',     'bob', 'Trace']
print(len(classmates))
classmates.append('Adgage')
classmates.insert(1,"Tdsg")
print(classmates)
classmates.pop()
classmates.pop(1)
print(classmates)

# tuple 元组，一旦初始化就不能够进行修改
classmates=('Nifs','Fdf',"FDfs")
print(classmates)

# 条件判断
age = 23
if age>4:
    print("yes")
elif age<0:
    print("summer")
else:
    print('no')

####  注意这里的输入，每次输入都是一个字符串，需要我们自己转化为整数才行的
# birth = input("请出入一个整数")
# birth = int(birth)
# if birth<2000:
#     print('less than 2000')
# else:
#     print('mora than 2000')


# 循环
# 注意！！！！range函数是需要range多一个数字的，range（101）就是1加到一百
sum=0
for i in range(101):
    sum=sum+i
print(sum)

for i in classmates:
    print(i)

sum=0
n=100
while n>0:
    sum+=n
    n-=1
print(sum)


# dictionary
d = {"Michael": '95', 'Bob': 75, 'Tracy': 85}
d['Michael'] = 2324
print(d['Michael'])

# set:要创建一个set需要提供一个list作为输入集合
# set:使用add 函数，remove函数进行添加元素，删除元素
# 因为是一个有序的集合，所以就自然而然操作就少了
s = set([2,2,2,2,2,434,5,'56565'])
print(s)
