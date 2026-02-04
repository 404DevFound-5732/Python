def str_reverse(s):
    """
    str_reverse 的 Docstring
    
    :param s: 讲被反转的字符串
    :return: 反转后的字符串
    """
    return print(s[::-1])

def substr(s, x, y):
    """
    substr 的 Docstring
    
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束的下标
    """

    return s[x:y]

if __name__ == "__main__":
    print(str_reverse("GOOD DAY"))
    print(substr("GOOD day",1,3))