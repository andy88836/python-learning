# Tuple(元组)与列表相似，不同之处在于元组的元素不能修改

info_tuple = ("zhangsan", 18, 1.75)
print(type(info_tuple))
print(info_tuple[0])

# 元组中只包含一个元素时，需要在元素后面加逗号 ,不然就是int类型
single_tuple = (5,)
print(type(single_tuple))