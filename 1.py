#定义全局变量money name
money=5000000
name=None

#要求客户输入姓名
name=input("请输入您的姓名:")

#定义查询函数
def query(show_header):
    if show_header:
        print("------------查询余额-----------")
    print(f"{name},您好，你的余额剩余：{money}元")

#定义存款函数
def saving(num):
    global money
    money+=num
    print("------------存款------------")
    print(f"{name}，您好，您存款{num}元成功")

#调用query函数查询余额
    query(False)

#定义取款函数
def get_money(num):
    global money
    money-=num
    print(f"{name},您好，您取款{num}元成功。")

    query(False)

def main():
    print("--------------主菜单---------")
    print(f"{name},您好，欢迎来到yyh银行，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")#使用制表符\t对齐
    print("退出\t\t【输入4】")
    return input("请输入您的选择:")

while True:
    keyboard_input=main()
    if keyboard_input=='1':
        query(True)
        continue    #通过continue继续下一次循环
    elif keyboard_input=='2':
        num=int(input("请输入存款金额："))
        saving(num)
        continue
    elif keyboard_input=='3':
        num=int(input("请输入取款金额："))
        get_money(num)
        continue
    else:
        print("程序退出啦")
        break


