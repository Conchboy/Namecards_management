# 显示菜单函数
card_dict = {}


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

    if len(card_dict) == 0:
        print("当前没有任何名片信息，请使用新增功能添加名片")
        # return关键字可以返回一个函数的执行结果
        # return下方的代码不会被执行，直接结束函数跳出
        return
    print("显示全部")
    for card_title in ["姓名", "QQ号码", "电话号码", "邮箱"]:
        print("%s\t\t" % card_title, end="")
    print("")
    # 打印分隔线

    print("*" * 40)
    # 遍历名片字典依次输出信息
    print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                     card_dict["QQ"],
                                     card_dict["phone"],
                                     card_dict["E-mail"]))


def search_card():
    """查询名片"""
    print("-" * 40)
    print("查询名片")
    # 1. 提示用户输入需要查询的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2. 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_list in card_dict:
        if find_name == card_list["name"]:
            print("姓名\t\tQQ\t\t电话\t\t邮箱")
            print("*" * 40)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                     card_dict["QQ"],
                                     card_dict["phone"],
                                     card_dict["E-mail"]))



            break
    else:
        print("抱歉没有找到 %s" % find_name)


