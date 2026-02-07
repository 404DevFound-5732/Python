from data_define import Recode
import json
class FileReader:

    def read_data(self) -> list[Recode]:
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path

    def read_data(self) ->list[Recode]:
        f = open(self.path,"r",encoding="UTF-8")

        read_list: list[Recode] = []        
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            read = Recode(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            read_list.append(read)
        f.close()    
        return read_list
    
class JsonFileReader(FileReader):

    
    def __init__(self,path):
        self.path = path

    def read_data(self) ->list[Recode]:
        f = open(self.path,"r",encoding="UTF-8")

        read_list: list[Recode] = []        
        for line in f.readlines():
            data_dict = json.loads(line)
            recode = Recode(data_dict["date"], data_dict["order-id"], data_dict["money"], data_dict["province"])
            read_list.append(recode)

        f.close()
        return read_list
    

if __name__ == "__main__":
    text_file_reader = TextFileReader(r"D:\桌面文件\eg1.txt")
    list1 = text_file_reader.read_data()
    json_file_reader = JsonFileReader(r"D:\桌面文件\eg2.txt")
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)