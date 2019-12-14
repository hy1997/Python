Bill = True
knife = "水瓶"
knife_length = 30
# if嵌套语句
if Bill:
    print("有火车票，需要安检")
    if knife == "刀子":
        if knife_length > 20:
            print("太长了，%d" % knife_length)
            print("不允许上车")
        else:
            print("可以带长度为 %d 可以进入" % knife_length)
    elif knife == "水瓶":
        print("可以带%s进入" % knife)
    else:
        print("什么都没带")
else:
    print("没有火车票")
