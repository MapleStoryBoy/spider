import cards_input

# 所有名片记录的列表
card_list = []


def show_menu():

    """显示菜单
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新建名片
    """
    print("-" * 50)
    print("功能：新建名片")

    # 1. 提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入 QQ 号码：")
    email = input("请输入邮箱：")

    # 2. 将用户信息保存到一个字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}

    # 3. 将用户字典添加到名片列表
    card_list.append(card_dict)

    # print(card_list)

    # 4. 提示添加成功信息
    print("成功添加 %s 的名片" % card_dict["name"])


def show_all():

    """显示全部
    """
    print("-" * 50)
    print("功能：显示全部")

    # 1. 判断是否有名片记录
    if len(card_list) == 0:
        print("提示：没有任何名片记录")

        return

    # 2. 显示所有名片
    print("姓名\t\t电话\t\tQQ\t\t邮箱")
    print("-" * 60)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["name"],
            card_dict["phone"],
            card_dict["qq"],
            card_dict["email"]))

    print("-" * 60)


def search_card():

    """搜索名片
    """
    print("-" * 50)
    print("功能：搜索名片")

    # 1. 提示要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2. 遍历字典
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 60)

            print("%s\t\t%s\t\t%s\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["qq"],
                card_dict["email"]))

            print("-" * 60)

            deal_card(card_dict)

            break
    else:
        print("没有找到 %s" % find_name)


def deal_card(find_dict):

    """操作搜索到的名片字典

    :param find_dict:名片字典
    """

    action_str = input("请输入对名片的操作：1: 修改/ 2: 删除/ 0: 返回上级菜单")

    if action_str == "1":

        find_dict["name"] = cards_input.input_card_info(find_dict["name"],
                                                        "请输入姓名[回车不修改]：")
        find_dict["phone"] = cards_input.input_card_info(find_dict["phone"],
                                                         "请输入电话[回车不修改]：")
        find_dict["qq"] = cards_input.input_card_info(find_dict["qq"],
                                                      "请输入QQ[回车不修改]：")
        find_dict["email"] = cards_input.input_card_info(find_dict["email"],
                                                         "请输入邮箱[回车不修改]：")

        print("%s 的名片修改成功！" % find_dict["name"])
    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功！")
