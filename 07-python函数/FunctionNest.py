def test1():
    test2()
    print("*" * 50)
    test2()


def test2():
    print("-" * 50)


test1()
