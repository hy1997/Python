# if条件语句
age = int(input("请输入年龄："))

# >= (大于等于)
# ==（等于）
# != (不等于)
# <(小于)
# <= （小于等于）
# 比较运算符

if age >= 18:
    print("可以进入")
else:
    print("不能进入")

print("执行！")


if age >= 38:
    print("可以进入")
elif age >= 20:
    print("不能进入")

print("执行！")
