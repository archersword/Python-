# -*- codeing =utf-8 -*-
# @time :2021/1/20 19:44
# @Author: hrf
# @File: Jiujiu.py
# @software:PyCharm


# 实现一个九九乘法表


#第一种写法：
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

#第二种写法：

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
