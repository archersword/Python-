# -*- codeing =utf-8 -*-
# @time :2021/1/19 11:22
# @Author: hrf
# @File: demo2.py
# @software:PyCharm

# if 100:

    # if 后面直接加判断语句，不需要括号，记住加冒号
    # 同时，if后面的输出必须缩进，表示的是该输出属于if的部分
if 0:
    print("true")
else:
    print("false")

print("end")


#
# #输入一个学生的成绩，判断他是属于哪一个等级
# score=int(input("you score is:"))
# #问题：比较大小要是整型变量才有大小之分，所以input需要强制转化，input默认是字符串类型，没有大小之分
#
# if score>=90 and score<=100:
#     print("you score is A")
# else:
#     if score>=80 and score<90:
#         print("you score is B")
#     else:
#         if score>=70 and score<80:
#             print("you score is C")
#         else:
#             if score>=60 and score<70:
#                 print("you score is D")
#             else:
#                 print("you score is E")
#     print("end")


# score=87
# if score>=90 and score<=100:
#      print("you score is A")
# elif score>=80 and score<=90:
#      print("you score is B")
# else:
#      print("you score is E")
#      # elif实现的是多分支的选项，他和if、else是相同级别的语句
#      # elif可以让条件选择更加直观方便，不需要嵌套，直接对输入进行判断，如果不行就进入下一个判断
#      # 直到满足条件，即可跳出循环
#
# # 使用elif，而不是嵌套的分数等级评定方法：
# score=int(input("enter your score:"))
# if score>=90 and score<=100:
#     print("you score is A")
# elif score>=80 and score<=90:
#     print("you score is B")
# elif score >=70 and score<=80:
#     print("you score is C")
# elif score>=60 and score<=70:
#     print("you scroe is D")
# else:
#     print("you score is E")
#
# xingbie=1  #nan:1 nv:0
# dansheng=1  #dansheng:1 youpenyou:0
#
# if xingbie==1:
#     print("male")
#     if dansheng==1:
#         print("to you")
#     else:
#         print("end")
# else:
#     print("female")
#     print("end")




import random #引入随机数，这是一种第三方库

x=random.randint(0,2) #随机数的用法：此语句表示：随机输出0到2之间的任意整数，包括0,1,2
print(x)

#


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


a=int(input("请输入我方出拳"))
b=random.randint(0,2)
print("对方出拳为%d"%b)

if a!=0 and a!=1 and a!=2:
    print("输入错误，请重新出拳")
else:

    if a==0 and b==2:
        print("你赢了")
    elif a==2 and b==0:
        print("你输了")
    elif a==b:
        print("打了平手，要不再来一次？")
    elif a>b:
        print("你赢了")
    else :
        print("你输了")