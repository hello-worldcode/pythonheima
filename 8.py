#匿名函数
#函数作为参数传递
def test_func(compute):
    result=compute(1,2)
    print(result)
def compute(x,y):
    return x+y
