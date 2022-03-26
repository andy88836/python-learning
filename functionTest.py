# import multipleTable
# multipleTable.multiple_table()


def sum_2_num(num1, num2):
    # num1 = int(input("请输入数字1"))
    # num2 = int(input("请输入数字2"))
    result = num1 + num2
    # print("%d + %d  = %d" % (num1, num2, result))
    return result  # 有返回值，需要使用变量来接受函数执行返回的结果


sum_result = sum_2_num(10, 20)
print("计算结果: %d" % sum_result)
