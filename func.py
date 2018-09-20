def func1():
    print('I am a Function1')

def func2(arg1, arg2):
    print(arg1, ' ', arg2)
    return arg1, arg2

def cube(x):
    return x*x*x

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
# func1()
# print(func1())
# print(func1)

# func2(10, 20)
# print(func2(10, 20))
# print(cube(3))

print(power(2))
print(power(2, 12))
print(power(x=3, num=2))

print(multi_add(4, 5, 10))
