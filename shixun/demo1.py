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
#d 整数 %s 字符串

#-------以下两个为重点内容
age=18
print("我的名字是%s,我的国籍是%s"%("小张","中国"))
#输出多个字符时，可以通过%将后面的单词与前面相对应
print("我的年纪是：%d岁"%age)
#----------

#补充部分
print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
#后期的点将前面的字符分隔开来
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")