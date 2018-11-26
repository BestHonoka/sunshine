

import cards_tools
while True:
    cards_tools.show_menu()
    action_str=input("请输入你的选择: ")
    print ("你选的操作是：",action_str)
    # 1,2,3是名片操作，0是推出，其他错误
    if action_str in ["1","2","3"]:
        if action_str =="1":
            cards_tools.new_card()
        elif action_str =="2":
            cards_tools.show_all()
        elif action_str =="3":
            cards_tools.search_card()

    elif action_str == "0":
        print ("欢迎再次使用《名片系统》")
        break
        #pass
    else:
        print ("输入有误。")