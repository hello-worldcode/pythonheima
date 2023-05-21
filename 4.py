#数据容器的入门
#name_list=[“a","b","c","d"]
#一种可以容纳多份数据的数据类型 每一份数据成为一个元素
#每一个元素，可以是任意类型的数据

#1.列表  []
name_list=["itheima","itcast","python"]
print(name_list)
print(type(name_list))

my_list=[[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))

my_list=[]
print(type(my_list))
#使用列表的下标索引
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

my_list=[[1,2,3],[123]]
print(my_list[-2][-2])

print(name_list[::2])

#列表一种类，面向对象，列表有方法 对象 属性
my_list=["宫倾","桃李不言","师说"]
index=my_list.index("宫倾")
print(index)
index=my_list.index("桃李不言")
print(index)
my_list[1]='余生为期'#列表中元素的修改
print(my_list[1])
for i in my_list:
    print(i,end=" ")
print()

my_list.insert(3,"桃李不言")#列表中元素的插入 前插
for i in my_list:
    print(i,end=" ")

print("")
my_list.append("桃李不言")#列表元素 append尾插
for i in my_list:
    print(i,end=" ")

print()
my_list.extend(["探虚陵","有趣"])#extend 追加容器中的一批
for i in my_list:
    print(i,end=" ")

print()
del(my_list[3])
for i in my_list:
    print(i,end=" ")#del 删除列表元素

print("")
my_list.append("桃李不言")#列表元素 append尾插
for i in my_list:
    print(i,end=" ")

print("")
my_list.pop()
for i in my_list:
    print(i,end=" ")#pop可以传参数 默认弹出尾部
    #指定下标删除

#指定内容删除
my_list.remove("有趣")
print()
for i in my_list:
    print(i,end=" ")

print()
print(my_list.count("有趣"))

my_list.clear()

print("清空：")
for i in my_list:
    print(i,end=" ")

print(len(my_list))
#method
my_list.count()
my_list.__annotations__
my_list.__class__
if my_list:


#数量多
#混装
#允许重复元素
#可以追加修改删除