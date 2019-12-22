
# 字符串判断相关
"""
.ljust(width)     # 获取固定长度，左对齐，右边不够用空格补齐
.rjust(width)     # 获取固定长度，右对齐，左边不够用空格补齐
.center(width)  # 获取固定长度，中间对齐，两边不够用空格补齐
.zfill(width)      # 获取固定长度，右对齐，左边不足用0补齐
"""
poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一城楼"
]

for perm_str in poem:
    print(perm_str.center(10, " "))  # 获取固定长度，左对齐，右边不够用空格补齐

#
# print("!")
# print(perm_str.rjust(10))  # 获取固定长度，右对齐，左边不够用空格补齐
# print("!")
# print(perm_str.center(10)) # 获取固定长度，中间对齐，两边不够用空格补齐
# print("!")
# print(perm_str.zfill(10))  # 获取固定长度，右对齐，左边不足用0补齐

