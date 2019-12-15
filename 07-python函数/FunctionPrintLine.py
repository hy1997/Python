

def print_line(char, times):
    print(char*times)


def print_lines(char, times):
    i = 0
    while i < 5:
        print_line(char, times)
        i += 1


print_lines("+", 20)
