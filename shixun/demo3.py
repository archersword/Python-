# -*- codeing =utf-8 -*-
# @time :2021/1/19 16:27
# @Author: hrf
# @File: demo3.py
# @software:PyCharm


# for i in range(5):
#     print(i) # 和IF语句一样，属于for的语句需要缩进，这是要注意的格式

#
# for i in range(0,11,3):
#     print(i)
#
# for j in range(-10,-100,-30):
#     print(j)

# name="chengdu"
# for x in name:
#     print(x,end="\t")
#
# a=["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])

#
# y=[1,2,3,4,5,[1,2]]
# for i in y:
#     print(i)
# for使用于遍历某一个数据集，比如说在这里就是遍历了Y中的所有元素，
# i是循环变量，不需要循环多少次，只是将Y中的元素依次遍历。而且，for下面的语句是遍历一次就要执行的语句
#
# for j in range(5):
#     print(j)  range(5)表示从0到4的这样一个范围，记住，编程中的数组都是从0开始

#
# for i in range(0,10,3):
#     print(i)
#     # 表示从0到9这个范围内遍历，以3为一个单位步进
#
# for x in range(-10,-100,-30):
#     print(x)
#     表示从-10到-99遍历，步进值为-30，说明for可以使用于负数
#
# name="chengdu"
# for x in name:
#     print(x)
#     # for循环还可以遍历字符串，遍历每个字母
#
# a=[1,2,3,4,5]
#
# for x in a:
#     print(x)
#     遍历a这个列表中所有的元素
#
# for i in range(5):
#     print(i)
#
# for j in range(0,5):
#     print(j)
#
# x=range(5)
# print(x)
# print(type(x))
#
# for i in range(0,13,3):
#     print(i)
#     #
#     # # range(x,y,z)表示的是范围是从x到y-1，相邻元素之间的间隔为z。
#     # 所以此代码中从0到13才能输出12，而下面的从0到12无法输出12
#
# print("\t")
#
# for j in range(0,12,3):
#     print(j)
#
# 下面这部分还不理解，先放在这里：
# a=["aa","bb","cc","dd"]
# for i in range(len(a)):
#     print(i,a[i])
#
# i=0
# while i<5:
#     print(i)
#     i=i+1
# # 表示先判断i是否小于5，成立则执行后面的语句，否则跳出循环
# # 和其他的句子一样，后面的语句必须首行缩进，缩进的句子就是while成立需要执行的语句
# # 建议尽量使用for循环而不是while循环
#
# for j in range(5):
#     print(j)
    # 相同的可以使用for循环表示，但是没有死循环的风险
#


# sum=0
# for i in range(1,101):
#     print(i)
#     sum=sum+i
# print(sum)
#
# for循环和while在过程上有何不同？如何理解for循环的过程？

#
# sum=0
# j=1
# while j<=100:
#     sum=sum+j
#     j=j+1
# print(sum)
#
# counter=10
# while counter<5:
#     print(counter,"xiaoyu 5")
#     counter=counter+1
# else:
#     print(counter,"dayu dengyu 5")
#
#
#
# name=[2,14,23,156,2365,21,5,7123,3]
# for i in name:
#     if i==5:
#         break
#     # 在if条件判断中，如果符合条件则跳出整个循环体系，执行下一个不是循环的语句，这里就是130行
#     else:
#         print("we got %d" %i)
#     #  如果不满足if的条件判断，那么就执行else的语句
#     # 个人觉得，还是要把else写出来了，因为这样能够看清楚if判断之后代码的执行顺序，不容易混淆
# print("we end at%d"%i)


# 实现一个九九乘法表
#
# i=1
# j=1
# while i<=9:
#     while j<=9:
#         if j<=i:
#             num=i*j
#             print("%d*%d=%d "%(i,j,num),end="")
#             j=j+1
#         else:
#             print(end="\n")
#             j=1
#             break
#     i=i+1
# print(" we are end here")


i=1
j=1
for i in range(1,10):   # 遍历是指将集合中的元素都访问一遍，所以for循环就是按顺序访问集合，然后每访问一个数据，就执行一次语句，
                        # 这和传统预言的for循环有所不同
    j=1
    for j in range(1,10):
        if i>=j:
            num=i*j
            print("%d*%d=%d "%(i,j,num),end="")
        else:
            print(end="\n")
            break

print("we are end here")


