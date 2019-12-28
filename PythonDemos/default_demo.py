# 缺省参数 （默认值）
# def print_info(name, gender=True , title (后面的参数都要带缺省值)):
def print_info(name,title=True, gender=True):
    """

    :param name:
    :param title:
    :param gender:
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s %s" % (name, gender_text,title))


print_info("huyi",gender=False)
