# 手动抛异常
class User(object):
     user_name = None
     user_password = None

     def Login(self):
          self.user_name = input("请输入用户名：")
          self.user_password = input("请输入密码：")
          if len(self.user_password) <= 8:
               # print("主动抛出异常")
               # 创建异常对象
               ex = Exception("密码长度不够！")
               # 主动抛出异常
               return ex
          return  self.user_password



user = User()
print(user.Login())
