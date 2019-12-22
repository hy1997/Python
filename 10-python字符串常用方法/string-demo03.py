
# 查找
"""
.find()    # 搜索指定字符串，没有返回-1
.index()    # 同上，但是找不到会报错
.rfind()    # 从右边开始查找
.count()    # 统计指定的字符串出现的次数
字符串替换
.replace('old','new')    # 替换old为new
.replace('old','new',次数)    # 替换指定次数的old为new


字符串去空格及去指定字符

.strip()    # 去两边空格
.lstrip()    # 去左边空格
.rstrip()    # 去右边空格

.split()    # 默认按空格分隔
.split('指定字符')    # 按指定字符分割字符串为数组

"""
# 查找
s='hello world'
print(s.find('e'))  # 搜索指定字符串,没有返回-1
print(s.find('w',1,2))  # 顾头不顾尾，找不到则返回-1不会报错，找到了则显示索引
print(s.index('w',1,2)) # 同上，但是找不到会报错
print(s.count('o')) # 统计指定的字符串出现的次数
print(s.rfind('l')) # 从右边开始查找

# 替换 不会修改原有字符串内容  会产生一个新的字符串
s = 'hello world'
print(s.replace('world','python'))
print(s.replace('l','p',2))
print(s.replace('l','p',5))

# 字符串去空格及去指定字符

s='   h e-l lo   '
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.split('-'))
print(s.split())
