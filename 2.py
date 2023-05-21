str1="itheiam"
str2="sdf"
str3="fafdsafds"

#定义计数变量
cnt=0
for i in str1:
    cnt+=1
print(f"字符串{str1}的长度是{cnt}")


#for 循环无法被定义循环条件 和c++不同 for（ auto x: a) print (x)
#while 循环可以

#无法定义循环条件
#空格缩进很重要

def count_a(s):
    cnt=0
    for x in s:
        if x=='a':
            cnt+=1
    return cnt

print(f"{str1}中有{count_a(str1)}个a")

def hello():
    print("欢迎来到yyh家里做客！")

#定义函数func_b
def angry(choice):
    if(choice):
        print("气死我了")
    print("奸商！")

angry(False)