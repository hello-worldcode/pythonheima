#字面量 被写在代码中的固定值
#标识符 用户在编程时使用的名字

#函数的多返回值
def test_return():
    return 1, 2#允许多个返回值
x,y=test_return()
print(x,y)
#函数的多种传参方式

#位置参数
def user_info(name , age, gender):
    print()

#关键字参数

#缺省参数
def user_info(name,age=1,gender='男'):
    print(f"姓名是{name},年龄是{age},性别是{gender}")
#从右往左缺省
user_info("张三",2,"女")

#位置传递不定长
def user_info(*args):
    print(args)#元组容器
user_info("tom")
user_info('tom','18')

def user_info(*args):
    print(f"args参数类型是：{type(args)},内容时{args}")
user_info(1,2,3,'小明')