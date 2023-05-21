#变量在函数的作用域
# 局部变量
global num
num=100

def testA():
    global num
    num=200
    print(f"test_a:{num}")

def testB():
    num=300
    print(f"test_b:{num}")

def testC():
    print(f"test_c:{num}")
testA()
testB()
testC()
print(num)

#niubi 函数里面是无法修改外面
#我就是要在函数内部吧外面的全局变量给改变
#全局变量好像有点不一样

#局部变量 作用域在函数里面
#全局变量 作用域在函数里面和外面 相同名字也无法影响
#要先声明 global 才是同一个对象 否则是新的对象
