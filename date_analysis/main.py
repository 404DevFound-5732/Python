from data_define import Recode
from file_define import FileReader,TextFileReader,JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader(r"D:\桌面文件\eg1.txt")
json_file_reader = JsonFileReader(r"D:\桌面文件\eg2.txt")

Jan_data: list[Recode] = text_file_reader.read_data()
Feb_data: list[Recode] = json_file_reader.read_data()

all_data: list[Recode] = Jan_data + Feb_data

data_dict = {}
for recode in all_data:
    if recode.date in data_dict:
        data_dict[recode.date] += recode.money
    else:
        data_dict[recode.date] = recode.money

# --
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("sale",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="Dailysalesfigures")
)
bar.render("Daily_sales_chart.html")