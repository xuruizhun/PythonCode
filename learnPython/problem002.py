def my_abs(x):
    if x< 0:
        return -x
    else:
        return x

print(my_abs(-3434))

# 空函数
def nop():
    pass

# 同时返回多个值，其实就是返回tuple
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x,y = move(100,23,60 , math.pi/6)
print(x)
print(y)


# 默认参数的最大坑货
# 默认参数必须指向不变的参数
def add_end(L=[]):
    L.append('end')
    return L
print(add_end())
print(add_end())

# 切片操作
L = list(range(21))
print(L[1:4])
print(L[:8:3])
print(L[-5::2])

# 迭代器操作























