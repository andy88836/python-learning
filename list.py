name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list[2])

# 取索引
print(name_list.index("lisi"))

# 增加
# append是向列表的末尾增加数据
name_list.append("张三")
# insert需要说明插入数据的位置
name_list.insert(1, "李四")

temp_list = ["sunwukong", "zhubajie"]
name_list.extend(temp_list)

# 删除 如果被删除的元素有多个，删除第一个

name_list.remove("wangwu")
# pop删除列表中最后一个元素,也可删除指定位置的元素
name_list.pop()
name_list.pop(2)
# clear 清除列表
temp_list.clear()

# 使用del关键字来删除元素 del的本质是用来将一个变量从内存中删除的
del name_list[1]
print(name_list)
print(temp_list)



my_list = [ 1,4,3,2,5,7,5,9]
my_list.sort() # 升序排列
my_list.sort(reverse=True) # 降序排列
print(my_list)

# 迭代遍历
for my_name in name_list:
    print("我的名字叫：%s" % my_name)