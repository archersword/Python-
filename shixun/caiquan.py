# -*- codeing =utf-8 -*-
# @time :2021/1/19 15:59
# @Author: hrf
# @File: caiquan.py
# @software:PyCharm


import random #引入随机数，这是一种第三方库

x=random.randint(0,2) #随机数的用法：此语句表示：随机输出0到2之间的任意整数，包括0,1,2
print(x)

# 项目一：实现石头剪刀布猜拳效果
# 其中剪刀是0 石头是1 布是2
# 用户输入0-2中的一个数字，和系统随机生成的数字比较后得出结果
# 同时，对于输入不正常的情况要考虑全面，使程序能够正常运行


# #第一种程序：
# a=int(input("请输入我方出拳"))
# b=random.randint(0,2)
#
# print("对方出拳为%d"%b)
#
# if a!=0 and a!=1 and a!=2
#     print("请重新输入")
# else:
#
#
# if a==b:
#     print("平手")
# elif a==2:
#     if b==0:
#         print("你赢了")
#     else:
#         print("你输了")
# else:
#     if a==0 and b==2:
#         print("你输了")
#     else:
#         print("你输了")

# 以下为改进后的第二种程序，相比于第一种更加简单：
# 第一，将条件判断的过程简化，本项目中，0和2无法通过大小关系比较
# 所以需要将特殊情况单独判断，而且需要考虑到输入是否有误，还有就是Python需要对齐格式，
# 否则会出现无法运行的情况

import random # 引入随机数
a=int(input("请我方出拳"))
if a!=0 and a!=1 and a!=2:
        a=int(input("我方输入错误，请输入0、1或是2："))
else:
    print("")

b=random.randint(0,2)
print("对方出拳为%d"%b)

if a==0 and b==2:
    print("你赢了")
elif a==2 and b==0:
    print("你输了")
elif a==b:
    print("打了平手，要不再来一次？")
elif a>b:
    print("你赢了")
else:
    print("你输了")
