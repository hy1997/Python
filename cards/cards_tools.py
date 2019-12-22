def show_function():
    print("*************************************************")
    print("欢迎使用【名片管理系统】 v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*************************************************")


def add():
    name_str = str(input("请输入姓名:"))
    age_str = str(input("请输入年龄:"))
    QQ_str = str(input("请输入QQ:"))
    email_str = str(input("请输入邮箱:"))
    cards = {
        "name": name_str,
        "age": age_str,
        "QQ": QQ_str,
        "email": email_str
    }
    return cards


def show(cards_list):
    if len(cards_list) != 0:
        for cards in cards_list:
            for card in cards:
                print("%s ：%s" % (card, cards[card]))
    else:
        print("不存在卡片！请添加卡片")


def search(cards_list):
    search_info = str(input("请选择需要搜索的姓名:"))
    for cards in cards_list:
        if search_info == cards["name"]:
            for card in cards:
                print("%s ：%s" % (card, cards[card]))
            else:
                deal_card(cards, cards_list)
        else:
            print("抱歉没有找到！")


def deal_card(cards, cards_list):
    operation_str = str(input("您希望进行的操作  0 返回 1 删除 2 修改  ! "))
    if operation_str == "0":
        return
    elif operation_str == "1":
        cards_list.remove(cards)
        print("删除成功！")
    elif operation_str == "2":
        cards["name"] = input_card_info(cards["name"], str(input("请输入姓名:")))
        cards["age"] = input_card_info(cards["age"], str(input("请输入年龄:")))
        cards["QQ"] = input_card_info(cards["QQ"], str(input("请输入QQ:")))
        cards["email"] = input_card_info(cards["email"], str(input("请输入email:")))
        print("修改成功！")


def input_card_info(card, input_value):
    # 提示用户输入内容
    if len(input_value) > 0:
        return input_value
    else:
        return card

