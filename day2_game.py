import random
secret = random.randint(1,100)
guess = 0
attempts = 0
print("猜数字游戏开始！")
print("我已经想好了一个1到100之间的数字。")
while guess != secret:
    try:
        guess = int(input("请输入你猜的数字："))
    except ValueError:
        print("请输入一个有效的数！")
        continue
    attempts +=1
    if guess<secret:
        print("太小了，再大一点！")
    elif guess>secret:
        print("太大了，再小一点！")
print(f"恭喜你猜对了！答案就是{secret}")
print(f"你一共猜了{attempts}次。")
