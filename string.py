hello_str = "hello hello"

print(len(hello_str))

print(hello_str.count("h"))

# 三个判断是否只包含数字
hello_str.isnumeric() # 中文的也能判断 从下到上判断范围增大
hello_str.isdigit() # 可以判断ASCII码
hello_str.isdecimal()

# 判断以指定字符串开始
print(hello_str.startswith("hello"))
print(hello_str.endswith("hello"))
# 查找指定字符串
print(hello_str.find("llo"))
# index如果指定的字符串不存在，会报错，find查找的指定字符串不存在，会返回-1
# print(hello_str.index("lol"))
print(hello_str.find("bssc"))

# 替换字符串
# 注意！ replace不会修改原有字符串内容
print(hello_str.replace("hello","python"))
print(hello_str)

# 去除空白字符 string.lstrip  string.rstrip   string.strip
test_str = " hello python "
print(test_str)
print(test_str.strip())


# 字符串的拆分和拼接
# string.split(str="", num) 其中str默认包含'\r','\t','\n'和空格
my_str = "Do not\ngo gentle\t into that\n good night"
print(my_str)
my_list = my_str.split()
print(my_list)


#拼接：string.join(seq) 以string作为分隔符，将seq中的所有元素（的字符串表示）合并为一个新的字符串
#合并字符串 my_list是一个列表，列表没有join方法，只有字符串有join方法
result = " ".join(my_list)
print(result)

# 指定分割的num，则仅分隔num+1个子字符串
print(result.split(" ", 3))


# 字符串切片
num_str = "0123456789"
print(num_str[2:6])
print((num_str[2:]))
print(num_str[:6])
print(num_str[:])
print(num_str[::2])  # [开始：结束（不包含）：步长]
print(num_str[1::2])
print(num_str[-1])
print(num_str[2:-1])
print(num_str[-2:])
# 把步长设置为-1，则切片时倒着走
print(num_str[0::-1])

# 用切片把字符串倒过来
print(num_str[-1::-1])
print(num_str[::-1])

# append方法
t_list = [1,2,3,4]

t_list.append([8,9]) # 把[8，9]当作一个元素添加到列表的末尾
print(t_list)

# extend方法  把5，6当作两个元素添加到列表中
t_list.extend([5, 6])
print(t_list)