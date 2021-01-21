# 显示菜单函数
card_dict ={}
def show_menu():
    """显示菜单"""
    print("*" * 40)
    print("欢迎使用【名片管理系统】 V 0.1")
    print("")
    print("1. 新增名片\n2. 显示名片\n3. 名片查询\n")
    print("0. 退出系统")
    print("*" * 40)


def new_card():
    """新增名片"""
    print("-" * 40)
    print("新增名片")
    print("请输入名片的信息：")
    name_char = input("请输入名字：")
    qq_char = input("请输入QQ号码：")
    phone_char = input("请输入电话号码：")
    email_char = input("请输入电子邮件地址：")
    card_dict = {"name": name_char, "QQ": qq_char, "phone": phone_char, "E-mail": email_char}
    print("谢谢输入，新增的名片是： % s" % card_dict)


def show_all():
    """显示全部"""
    print("-" * 40)
    print("显示全部")
    for card_title in ["姓名", "QQ号码", "电话号码", "Email"]:
        print("%s\t\t" % card_title, end="")
    print("")
    # (card_dict["name"], card_dict["QQ"], card_dict["phone"], card_dict["E-mail"])
    print("*" * 40)





def search_card():
    """查询名片"""
    print("-" * 40)
    print("查询名片")




