number = 0
result = 0
print("开始计算")
while number <= 100:
    number += 1
    if number % 2 == 0:
        print("%d 是偶数" % number)
        result += number
    else:
        print("%d 不是偶数" % number)
print(result)
