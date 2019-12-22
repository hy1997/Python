studentS = [
    {
        "name":"张三",
        "age": "12"
    },
    {
        "name":"李四",
        "age": "42"
    }
]
find_name = "11"

for s in studentS:
    if s["name"] == find_name:
        print("找到了 %s " % s["name"])
        break
else:
    print("没有找到 %s" % find_name)
