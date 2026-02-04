money = 50000
name = input("请输入您的姓名： ")
def check():
    print("---------------查询余额---------------")
    
    print(f"{name},您好，您的余额为：{money}")

def saving(money1):
    #存款
    print("---------------存款---------------")
    global money 
    money= money + money1
    print(f"{name},您好，您存款{money1}成功\n您目前的月为{money}")

def query(money2):
    
    print("---------------取款---------------")
    global money
    money = money - money2
    if money < money1:
        print(f"您的账户余额不足，您的余额为{money}")
    else:
        print(f"{name},您好，您存款{money2}成功\n您目前的余额为{money}")

def main():
    
    print("---------------主菜单---------------")
    print(f"{name},您好，欢迎来到ATM,请您选择操作：")
    print("查询余额\t请输入【1】")
    print("存款\t\t请输入【2】")
    print("取款\t\t请输入【3】")
    print("退出\t\t请输入【4】")
    return input("请输入您的选择：")
while True:
    choice = main()
    if choice == "1":
        check()
        continue
    elif choice == "2":
        money1=int(input("请输入存款金额："))
        saving(money1)
        continue
    elif choice == "3":
        money2=int(input("请输入取款金额"))
        query(money2)
        continue
    elif choice == "4":
        break
    else:
        print("错误的数字！")




