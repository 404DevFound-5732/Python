class Recode:
     def __init__(self,date,order_id,money,province):
          """
          __init__ 的 Docstring
          功能：接受数据
          :param self: 
          :param date: 说明
          :param order_id: 说明
          :param money: 说明
          :param province: 说明
          """


          self.date = date
          self.order_id = order_id
          self.money = money
          self.province = province

     def __str__(self):
          return (f"{self.date},{self.order_id},{self.money},{self.province}")