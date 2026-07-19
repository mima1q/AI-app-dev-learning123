todos=[]
def show_menu():
    print("\n 待办事务管理工具")
    print("命令：add|list|done|delete|exit")
def add_task():
    task=input("请输入待办事项内容：").strip()
    if task=="":
        print("内容不能为空")
    else:
        todos.append({
            "id":len(todos)+1,
            "task":task,
            "done":False
        })
        print(f"已添加待办事项：{task}")
def list_task():
    if len(todos)==0:
        print("暂无待办事项")
    else:
        print("当前待办列表：")
        for  item in todos:
            status="已完成"if item["done"] else "未完成"
            print(f"  {status} [{item['id']}] {item['task']}")
def mark_done():
    try:
        id_num=int(input("请输入要标记为已完成的事项编号："))
        for item in todos:
            if item["id"]==id_num:
                item["done"]=True
                print(f"已标记完成：{item['task']}")
                break
            else:
                print("未找到对应的待办事项编号。")
    except ValueError:
        print("请输入一个有效的编号！")
def delete_task():
    try:
        id_num=int(input("请输入要删除的待办事项编号："))
        for i,item in enumerate(todos):
            if item["id"]==id_num:
                del todos[i]
                print(f"已删除待办事项：{item['task']}")
                break
        else:
            print("未找到对应的待办事项编号。")
    except ValueError:
        print("请输入一个有效的编号！")
def main():
    show_menu()
    while  True:
        command=input("\n请输入命令：").strip().lower()
        if command=="add":
            add_task()
        elif command=="list":
            list_task()
        elif command=="done":
            mark_done()
        elif command=="delete":
            delete_task()
        elif command=="exit":
            print("感谢使用待办事务管理工具！")
            break
        else:
            print("无效命令，请重新输入。")
if __name__=="__main__":
    main()  