todos=[]
print("待办事项管理工具")
print("命令:add|list|done|delete|exit")
while True:
    command=input("\n请输入命令：").strip().lower()
    if command=="add":
        task=input("请输入待办事项内容：").strip()
        todos.append({
            "id":len(todos)+1,
            "task":task,
            "done":False
        })
        print(f"已添加待办事项：{task}")
    elif command=="list":
        if len(todos)==0:
            print("当前没有待办事项。")
        else:
            print("当前待办列表：")
            for item in todos:
                status="已完成" if item["done"] else "未完成"
                print(f"  {status} [{item['id']}]{item['task']}")
    elif command=="done":
        try:
            id=int(input("请输入要标记为已完成的待办事项编号："))       
            for item in todos:
                if item["id"]==id:
                  item["done"]=True
                  print(f"已标记完成：{item['task']}")
                  break
            else:
               print("未找到对应的待办事项编号。") 
        except ValueError:
            print("请输入一个有效的编号！")
    
    elif command=="delete":
        try:
            id=int(input("请输入要删除的待办事项编号："))
            for i,item in enumerate(todos):
                if item["id"]==id:
                    del todos[i]
                    print(f"已删除待办事项：{item['task']}")
                    break
            else:
                print("未找到对应的待办事项编号。")
        except ValueError:
            print("请输入一个有效的编号！")
    elif command=="exit":
        print("退出待办事项管理工具。")
        break
    else:
        print("无效的命令，请重新输入。")