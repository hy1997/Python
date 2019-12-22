#!Users/HY/AppData/Local/Programs/Python/Python38


# pass 表示一个占位符
import cards_tools
cards_list = []

while True:
    cards_tools.show_function()
    action_str = input("请选择希望执行的操作：")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards = cards_tools.add()
            cards_list.append(cards)
            print("添加成功")
        elif action_str == "2":
            cards_tools.show(cards_list)
        elif action_str == "3":
            cards_tools.search(cards_list)

    elif action_str in "0":
        print("欢迎再次使用名片管理系统")
        break
    else:
        print("请选择正确的执行命令")
        break
