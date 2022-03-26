def multiple_table():
    """对函数的注释用三对双引号！！  函数的定义上方要有两行空行"""

    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col,row,col * row), end="\t") # \t输入一个制表符，协助在输出文本时垂直方向保持对齐
            col += 1
        print("")




        row += 1