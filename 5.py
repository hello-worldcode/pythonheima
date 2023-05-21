#2.元组（不可修改）
a=(1,2,3)
print(a)
print(a.count(2))#关键字 字面量 变量
b=()
print(f"a的类型是{type(a)}")

t4=("hello")
t5=("hello",)
print(f"t4的类型是{type(t4)}")
print(f"t4的类型是{type(t5)}")

#单个元素除了括号还得在末尾加上逗号类型才是元组
#元素类型不受限

t1=("仓鼠","蛇")
print(t1[0])

t2=(["itheima","ittest"],)
print(t2)
t2[0][0]="IT黑马"
print(t2)

#混装
#支持下标索引
#允许重复数据
#不允许修改

t=("周杰伦",11,["football","music"],)
print(t.index(11))
print(t[0])
del t[2][0]
print(t)
t[2].append("coding")
print(t)