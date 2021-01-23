# -*- coding =utf-8 -*-
# @time :2021/1/21 12:45
# @Author: hrf
# @File: baidu.py
# @software:PyCharm

# 通过调用第三方库完成一个简单的二维码

from MyQR import myqr

myqr.run(
    words="https://www.baidu.com",
    version=1,
    level="H",
    picture="C:\\Users\\archerswords\\Desktop\\python sucai\\pingru.gif",
    colorized=True,
    save_name="test.gif",
    save_dir="C:\\Users\\archerswords\\Desktop"
)

