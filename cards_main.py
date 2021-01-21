# 名片管理主程序
import cards_tools

while True:
    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择您希望执行的从操作：")
    print("您选择的操作是 【%s】" % action_str)

    # 针对 1,2,3 的名片操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        if action_str == "2":
            cards_tools.show_all()
        # 查询名片
        if action_str == "3":
            cards_tools.search_card()

        # 如果在开发程序时，不想立刻编写分支内部的代码，可以使用pass关键字
        # 表示一个占位符，能够保证程序的代码结构正确
        # 程序运行时，pass 关键字不会执行任何操作
        pass

    # 如果输入是0，那么退出
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他输入显示内容错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择。")

