# 显示菜单函数
card_list = []
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
    card_dict = {"name": name_char, "QQ": qq_char, "phone": phone_char, "Email": email_char}
    card_list.append(card_dict)
    print("谢谢输入，新增的名片是： % s" % card_dict)


def show_all():
    """显示全部"""
    print("-" * 40)

    if len(card_list) == 0:
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
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["QQ"],
                                        card_dict["phone"],
                                        card_dict["Email"]))


def search_card():
    """查询名片"""
    print("-" * 40)
    print("查询名片")
    # 1. 提示用户输入需要查询的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2. 遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\tQQ\t\t电话\t\t邮箱")
            print("*" * 40)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["QQ"],
                                            card_dict["phone"],
                                            card_dict["Email"]))
            # TODO 针对找到的名片记录执行谢盖和删除的操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到 %s" % find_name)


def deal_card(find_dict):

    print(find_dict)
    action_str = input("请输入对名片的操作："
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名【回车不修改】：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "QQ【回车不修改】：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话【回车不修改】：")
        find_dict["Email"] = input_card_info(find_dict["Email"], "邮箱【回车不修改】：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("名片已删除！")


def input_card_info(dict_value, tip_message):
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    # 2. 针对用户输入的内容进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3. 如果用户没有输入内容， 返回“字典中原有的值”
    else:
        return dict_value
