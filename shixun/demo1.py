#-*- codeing = utf-8 -*-
# @time :2021/1/18 21:07
# @Author: hrf
# @File: demo1.py
# @software:PyCharm


print("hello  world") #这是注释 单行注释
print("hello world")
'''
这是第一行注释
这是第二行注释
多行注释
'''
print("renhe ziufuchuan")
a=10
print(a)
print("zheshi bianliang",a)

#变量类型：和一般的变量一样，不能以数字开头，记得是大小写英文、数字和下划线组合
a=1
#赋值方法和c语言一样的
import keyword
keyword.kwlist

#格式化输出
age=18

#占位操作
print("我的年级是：%d 岁" %age)
age=age+1
print("nianji shi %d sui"%age)
age=age+1
print("nianjj shi %d sui"%age)
#格式化输出，将变量格式化输出，为了的是让变量能够变化的同时输出
#让%d占据输出的一部分，然后在把输出的变量引入后面

#如何输出字符串？
#先给一个变量命名，然后再输出变量，或是直接输出字符串
name="xiaozhang" #注意字符串需要用双引号括住，不需要给变量定义格式，直接赋值即可
print("name is %s" %name)
print("name is %s"%("xiaozhang"))
#%d 整数 %s 字符串

#def if else and  guanjianzi

#-------以下两个为重点内容
age=18
print("我的名字是%s,我的国籍是%s"%("小张","中国"))
#输出多个字符时，可以通过%将后面的单词与前面相对应
print("我的年纪是：%d岁"%age)
#----------

#补充部分print("aaa","bbb","ccc")f

print("www","baidu","com",sep=".")
#后期的点将前面的字符分隔开来
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")