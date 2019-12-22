
"""python中str函数isdigit、isdecimal、isnumeric的区别
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
"""

str = u"this2009";
print (str.isdecimal());
str = u"23443434";
print (str.isdecimal())
