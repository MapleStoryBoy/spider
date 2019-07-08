# 记录所有的名片字典
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)

    print(card_list)

    # 4. 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")


def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
