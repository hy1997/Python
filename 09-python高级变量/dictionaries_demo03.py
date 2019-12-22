# 字典类型 {} 表示  是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的不一样

# 列表里面放字典
#  java  List<Map> lists= new List<Map>();
card_lists = [
    {
        "name": "张三",
        "age": "20",
        "phone": "123123123",
        "qq": "111111111"
    },
    {
        "name": "李四",
        "age": "23",
        "phone": "2321312312",
        "qq": "222222222"
    },
    {
        "name": "王五",
        "age": "28",
        "phone": "2312123123",
        "qq": "33333333"
    }
]

# 迭代遍历字典
# 遍历K事每一次循环中获取的K值
for card in card_lists:
    print(card)
