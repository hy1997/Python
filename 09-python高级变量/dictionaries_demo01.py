# 字典类型 {} 表示  是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的不一样
persons = {
          "name": "胡怡",
          "age": 23,
          "gender": True,
          "address": "上海静安区"
          }
# 统计长度
print(len(persons))

# 合并字典
temp_dict = {
    "height": 1.75,
    "age": 25
}
persons.update(temp_dict)  # 注意有相同的元素会覆盖 比如 age元素

print(persons)

# 删除
persons.clear()
print(persons)
