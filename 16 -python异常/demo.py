try:
    num = int(input("请输入"))
    result = 8/num


except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")

# except Exception as result:
#     print("未知错误")
# except (ValueError,ZeroDivisionError):
#     print("捕获两个异常")
else:
    print("没有出现异常才会执行 else ")
finally:
    print("无论是否出现异常都会执行 finally" )
