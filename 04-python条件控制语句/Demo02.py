# and   or  not 逻辑运算服

age = int(input("请输入年龄！"))


# and 并且
if 0 <= age <= 120:
    print("可以进入！")
else:
    print("不能进入")

python_score = 80
java_score = 80


# or 或者！
if python_score > 60 or java_score > 60:
    print("通过")
else:
    print("不通过")


# not Java的取反！
is_emp = False
if not is_emp:
    print("非")
