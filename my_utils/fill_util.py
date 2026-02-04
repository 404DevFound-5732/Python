def print_file_info(file_name):
    """
    print_file_info 的 Docstring
    
    :param file_name: 接受传入的文件路径
    :return: 打印文件全部内容
    """
    f = None
    try:
       f = open(file_name,"r",encoding="UTF-8")
       conent = f.read()
       print(conent)
    except Exception as e:

        print(f"出现异常，原因是{e}")
        
    finally:
        if f:
            f.close()



def append_to_file(file_name, data):
    """
    append_to_file 的 Docstring
    功能：接收文件并追加数据
    :param file_name:指定接收文件路劲
    :param data: 添加数据
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    #print_file_info(r"D:\桌面文件\test.txt")
    append_to_file(r"D:\桌面文件\test.txt","hell world")