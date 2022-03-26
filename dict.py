xiaoming_dict = {"name" : "小明"}

#取值
print(xiaoming_dict["name"])

# 增加，修改
# xiaoming_dict["age"] = 18
# xiaoming_dict["name"] = "小小明"
#
# print(xiaoming_dict)
#
# # 删除
# xiaoming_dict.pop("name")
#
# print(xiaoming_dict)
#
# print(len(xiaoming_dict))
#
# temp_dict = {"height": 1.75}
# # 合并字典 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
# xiaoming_dict.update(temp_dict)
#
# print(xiaoming_dict)

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对key
xiaoming_dict = {"name" : "小明",
                 "qq" : "123456",
                 "phone" : "10086"}
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))