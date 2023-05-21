my_str="itheima itcast boxuegu"
it_count=my_str.count("it")
print(f"字符串内it的个数为：{my_str.count('it')}")
new_str=my_str.replace(" ","|")
print(f"替换后的字符串：{new_str}")
my_list=new_str.split("|")
print(f"分割字符串得到的列表：{my_list}")
