# 字典类型 {} 表示  是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的不一样
#  java 里面的Map
persons = {
          "name": "胡怡",
          "age": 23,
          "gender": True,
          "address": "上海静安区"
          }
# 取值
print(persons["name"])

# 新增 如果key不在就是新增
persons["weight"] = 140
# 修改 如果key存在就是修改
persons["name"] = "huyi"
#  删除
persons.pop("name")


for person in persons:
    print(person)
