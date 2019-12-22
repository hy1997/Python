"""
利用索引进行切片操作时，可包含三个参数:

如对列表来说即：list[start_index: stop_index: step]。

 起始位置 : start_index (空时默认为 0)。
 终点位置: stop_index (空时默认为列表长度) 需要注意起点与终点索引的位置关系。
 步长: step (空时默认为 1，不能为 0)
"""

num_str = "0123456789"

print(num_str[2:6])

print(num_str[:6])

print(num_str[2:])

print(num_str[:])

print(num_str[::2])

print(num_str[-1])

print(num_str[::-1])
