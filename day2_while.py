password="1234"
guess=input("请输入密码：")
while guess!=password:
    print("密码错误，再试一次！")
    guess=input("请输入密码：")
print("欢迎回来！")