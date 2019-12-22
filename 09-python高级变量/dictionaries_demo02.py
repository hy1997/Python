# 字典类型 {} 表示  是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的不一样
persons = {
          "name": "胡怡",
          "age": "23",
          "address": "上海静安区"
          }
# 迭代遍历字典
# 遍历K事每一次循环中获取的K值
for k in persons:
    print("%s - %s" %(k, persons[k]))
