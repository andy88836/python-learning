import random
com = random.randint(1,3);

my = int(input("请出拳"))
print("电脑出拳为%d" %com)
if my == com :
    print("平局")
elif my == 1 and com == 3:
    print("你输了！")
elif my < com :
    print("你赢了！")
elif my > com:
    print("你输了！")
elif my == 3 and com ==1:
    print("你赢了！")
